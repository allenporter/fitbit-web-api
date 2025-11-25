import asyncio
import json
import os
from collections.abc import AsyncGenerator, Callable
from typing import Any, Dict

import pytest
from aiohttp import web
from aiohttp.test_utils import TestServer

import fitbit_web_api


@pytest.fixture
async def loop() -> AsyncGenerator[asyncio.AbstractEventLoop, None]:
    """Event loop fixture for pytest-aiohttp."""
    yield asyncio.get_running_loop()


@pytest.fixture(name="responses")
def responses_fixture() -> Dict[str, Any]:
    """Fixture that holds mock GET responses for the server."""
    return {}


@pytest.fixture(name="requests")
def requests_fixture() -> list[tuple[str, dict[str, Any]]]:
    """Fixture that records GET requests made to the mock server."""
    return []


@pytest.fixture(name="post_responses")
def post_responses_fixture() -> Dict[str, Any]:
    """Fixture that holds mock POST responses for the server."""
    return {}


@pytest.fixture(name="post_requests")
def post_requests_fixture() -> list[tuple[str, dict[str, Any], dict[str, Any]]]:
    """Fixture that records POST requests made to the mock server."""
    return []


def _query_string_dict(query_string: str) -> Dict[str, str]:
    params = {}
    if query_string:
        for pair in query_string.split("&"):
            key, value = pair.split("=")
            params[key] = value
    return params


@pytest.fixture
async def fitbit_app(
    requests: list[tuple[str, dict[str, Any]]],
    responses: Dict[str, Any],
    post_requests: list[tuple[str, dict[str, Any], dict[str, Any]]],
    post_responses: Dict[str, Any],
) -> web.Application:
    async def handler(request: web.Request) -> web.Response:
        get_requests.append((request.path, _query_string_dict(request.query_string)))
        if request.path in responses:
            return web.json_response(responses[request.path])
        return web.Response(status=404)

    async def post_handler(request: web.Request) -> web.Response:
        body = await request.json() if request.can_read_body else {}
        post_requests.append(
            (request.path, _query_string_dict(request.query_string), body)
        )
        if request.path in post_responses:
            return web.json_response(post_responses[request.path])
        return web.Response(status=404)

    app = web.Application()
    app.router.add_get("/{tail:.*}", handler)
    app.router.add_post("/{tail:.*}", post_handler)
    return app


@pytest.fixture
async def fitbit_server(aiohttp_server: Any, fitbit_app: web.Application) -> TestServer:
    return await aiohttp_server(fitbit_app)


@pytest.fixture
async def api_client(
    fitbit_server: TestServer,
) -> AsyncGenerator[fitbit_web_api.ApiClient, None]:
    configuration = fitbit_web_api.Configuration(
        host=f"http://{fitbit_server.host}:{fitbit_server.port}"
    )
    async with fitbit_web_api.ApiClient(configuration) as api_client:
        yield api_client


@pytest.fixture
def load_test_data() -> Callable[[str], Any]:
    """Fixture to load test data from JSON files."""

    def _load(filename: str) -> Any:
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "testdata", filename)
        with open(file_path, "r") as f:
            return json.load(f)

    return _load
