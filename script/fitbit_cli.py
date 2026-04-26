#!/usr/bin/env python3
"""
Fitbit CLI Tool

Before using this tool, you must create a Fitbit App in the Fitbit Developer Portal:
1. Go to https://dev.fitbit.com/apps/new
2. Set the "OAuth 2.0 Application Type" to "Personal" (this allows access to intraday data).
3. Set the "Callback URL" to `http://127.0.0.1:8080` (or the port you plan to use).
   Note: Some setups require a trailing slash: `http://127.0.0.1:8080/`. If you get an invalid redirect URI error during login, try adding the trailing slash.

Set your credentials in your environment before running the login command:
    export FITBIT_CLIENT_ID="your_client_id"
    export FITBIT_CLIENT_SECRET="your_client_secret"
    uv run script/fitbit_cli.py login
"""

import argparse
import asyncio
import base64
import hashlib
import json
import logging
import os
import secrets
import sys
import urllib.parse
from contextlib import asynccontextmanager
from datetime import date as dt_date
from pathlib import Path
from typing import Any, AsyncGenerator

import aiohttp
from aiohttp import web

from fitbit_web_api.api.activity_api import ActivityApi
from fitbit_web_api.api.activity_time_series_api import ActivityTimeSeriesApi
from fitbit_web_api.api.body_api import BodyApi
from fitbit_web_api.api.body_time_series_api import BodyTimeSeriesApi
from fitbit_web_api.api.heart_rate_time_series_api import HeartRateTimeSeriesApi
from fitbit_web_api.api.sleep_api import SleepApi
from fitbit_web_api.api_client import ApiClient
from fitbit_web_api.configuration import Configuration

FITBIT_AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
FITBIT_TOKEN_URL = "https://api.fitbit.com/oauth2/token"


def setup_logging(debug: bool) -> None:
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def load_token(token_file: Path) -> dict[str, Any]:
    if not token_file.exists():
        print(
            f"No token found at {token_file}. Please run 'login' first.",
            file=sys.stderr,
        )
        sys.exit(1)
    return json.loads(token_file.read_text())


def save_token(token_file: Path, data: dict[str, Any]) -> None:
    token_file.parent.mkdir(parents=True, exist_ok=True)
    token_file.write_text(json.dumps(data, indent=2))
    print(f"Success! Token saved to {token_file}")


@asynccontextmanager
async def create_api_client(token_file_path: str) -> AsyncGenerator[ApiClient, None]:
    token_file = Path(token_file_path).expanduser()
    token_data = load_token(token_file)
    access_token = token_data.get("access_token")

    config = Configuration()
    config.access_token = access_token

    async with ApiClient(configuration=config) as api_client:
        yield api_client


async def do_login(
    client_id: str, client_secret: str, port: int, token_file: Path
) -> None:
    redirect_uri = f"http://127.0.0.1:{port}"
    code_verifier = secrets.token_urlsafe(96)

    code_challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode("ascii")).digest())
        .decode("ascii")
        .rstrip("=")
    )

    auth_params = {
        "client_id": client_id,
        "response_type": "code",
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "scope": "activity heartrate location nutrition profile settings sleep social weight",
        "redirect_uri": redirect_uri,
    }
    url = f"{FITBIT_AUTH_URL}?{urllib.parse.urlencode(auth_params)}"

    print(f"Please open the following URL in your browser to authorize:")
    print(f"\n  {url}\n")
    print(f"Listening on {redirect_uri} for the callback...")

    app = web.Application()
    auth_code = asyncio.Future()

    async def handle_callback(request: web.Request) -> web.Response:
        code = request.query.get("code")
        if code:
            auth_code.set_result(code)
            return web.Response(
                text="Authorization successful! You can close this window and return to the terminal."
            )
        else:
            err = request.query.get("error", "unknown error")
            auth_code.set_exception(RuntimeError(f"Authorization failed: {err}"))
            return web.Response(text=f"Authorization failed: {err}", status=400)

    app.add_routes([web.get("/", handle_callback)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "127.0.0.1", port)
    await site.start()

    try:
        code = await auth_code
    finally:
        await runner.cleanup()

    print("Exchanging authorization code for access token...")
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")

    async with aiohttp.ClientSession() as session:
        async with session.post(
            FITBIT_TOKEN_URL,
            headers={
                "Authorization": f"Basic {b64_auth}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "client_id": client_id,
                "grant_type": "authorization_code",
                "redirect_uri": redirect_uri,
                "code": code,
                "code_verifier": code_verifier,
            },
        ) as resp:
            data = await resp.json()
            if resp.status != 200:
                print(f"Failed to get token: {data}", file=sys.stderr)
                sys.exit(1)

            save_token(token_file, data)


async def do_query(args: argparse.Namespace) -> None:
    async with create_api_client(args.token_file) as api_client:
        date = args.date
        if date == "today":
            date = dt_date.today().isoformat()

        api_response = None

        if args.type == "activity":
            api = ActivityApi(api_client)
            print(f"Querying activity for date: {date}")
            api_response = await api.get_activities_by_date_with_http_info(
                var_date=date
            )
        elif args.type == "sleep":
            api = SleepApi(api_client)
            print(f"Querying sleep for date: {date}")
            api_response = await api.get_sleep_by_date_with_http_info(var_date=date)
        elif args.type == "body":
            api = BodyApi(api_client)
            print(f"Querying body weight for date: {date}")
            api_response = await api.get_weight_by_date_with_http_info(var_date=date)
        else:
            print(f"Unknown query type: {args.type}", file=sys.stderr)
            sys.exit(1)

        print("\n--- Response Status ---")
        print(api_response.status_code)

        if args.debug:
            print("\n--- Raw JSON Payload ---")
            raw_json = api_response.raw_data.decode("utf-8")
            try:
                parsed = json.loads(raw_json)
                print(json.dumps(parsed, indent=2))
            except json.JSONDecodeError:
                print(raw_json)
        else:
            print("\n--- Parsed Model ---")
            print(api_response.data)


async def do_time_series_query(args: argparse.Namespace) -> None:
    async with create_api_client(args.token_file) as api_client:
        date = args.date
        if date == "today":
            date = dt_date.today().isoformat()

        api_response = None

        if args.type == "activity":
            api = ActivityTimeSeriesApi(api_client)
            print(
                f"Querying activity time series '{args.resource}' for date: {date}, period: {args.period}"
            )
            api_response = (
                await api.get_activities_resource_by_date_period_with_http_info(
                    var_resource_path=args.resource, var_date=date, period=args.period
                )
            )
        elif args.type == "body":
            api = BodyTimeSeriesApi(api_client)
            print(
                f"Querying body time series '{args.resource}' for date: {date}, period: {args.period}"
            )
            api_response = await api.get_body_resource_by_date_period_with_http_info(
                var_resource_path=args.resource, var_date=date, period=args.period
            )
        elif args.type == "heartrate":
            api = HeartRateTimeSeriesApi(api_client)
            print(
                f"Querying heart rate time series for date: {date}, period: {args.period} (ignoring resource param)"
            )
            api_response = await api.get_heart_by_date_period_with_http_info(
                var_date=date, period=args.period
            )
        else:
            print(f"Unknown time-series query type: {args.type}", file=sys.stderr)
            sys.exit(1)

        print("\n--- Response Status ---")
        print(api_response.status_code)

        if args.debug:
            print("\n--- Raw JSON Payload ---")
            raw_json = api_response.raw_data.decode("utf-8")
            try:
                parsed = json.loads(raw_json)
                print(json.dumps(parsed, indent=2))
            except json.JSONDecodeError:
                print(raw_json)
        else:
            print("\n--- Parsed Model ---")
            print(api_response.data)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fitbit CLI Tool")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging and print raw JSON payloads",
    )
    parser.add_argument(
        "--token-file",
        default=os.environ.get("FITBIT_TOKEN_FILE", "~/.config/fitbit-token.json"),
        help="Path to save/load the OAuth token",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Login command
    login_parser = subparsers.add_parser(
        "login", help="Authenticate with Fitbit and save token locally"
    )
    login_parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Local port for OAuth callback (default: 8080)",
    )

    # Query command
    query_parser = subparsers.add_parser("query", help="Query Fitbit API endpoints")
    query_parser.add_argument(
        "type", choices=["activity", "sleep", "body"], help="Type of data to query"
    )
    query_parser.add_argument(
        "--date", default="today", help="Date to query (format YYYY-MM-DD or 'today')"
    )

    # Time-series command
    ts_parser = subparsers.add_parser(
        "time-series", help="Query Fitbit Time Series API endpoints"
    )
    ts_parser.add_argument(
        "type",
        choices=["activity", "body", "heartrate"],
        help="Type of time series data to query",
    )
    ts_parser.add_argument(
        "resource",
        help="Resource path (e.g., 'steps', 'calories' for activity; 'weight', 'fat' for body; 'heart' for heartrate)",
    )
    ts_parser.add_argument(
        "--date",
        default="today",
        help="End date to query (format YYYY-MM-DD or 'today')",
    )
    ts_parser.add_argument(
        "--period",
        default="1m",
        help="Range (e.g., 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max)",
    )

    args = parser.parse_args()

    setup_logging(args.debug)

    if args.command == "login":
        client_id = os.environ.get("FITBIT_CLIENT_ID")
        client_secret = os.environ.get("FITBIT_CLIENT_SECRET")
        if not client_id or not client_secret:
            print(
                "Error: FITBIT_CLIENT_ID and FITBIT_CLIENT_SECRET environment variables are required for login.",
                file=sys.stderr,
            )
            sys.exit(1)
        token_file = Path(args.token_file).expanduser()
        asyncio.run(do_login(client_id, client_secret, args.port, token_file))
    elif args.command == "query":
        asyncio.run(do_query(args))
    elif args.command == "time-series":
        asyncio.run(do_time_series_query(args))


if __name__ == "__main__":
    main()
