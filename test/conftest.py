import asyncio
import json
import logging
import os
from collections.abc import AsyncGenerator, Awaitable, Callable
from typing import Any, Dict
import logging
import os
from collections.abc import AsyncGenerator, Awaitable, Callable
from typing import Any, Dict

import aiohttp
import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient, TestServer

import fitbit_web_api

_LOGGER = logging.getLogger(__name__)

TEST_HOST = "https://api.fitbit.com"


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


@pytest.fixture(name="delete_responses")
def delete_responses_fixture() -> Dict[str, Any]:
    """Fixture that holds mock DELETE responses for the server."""
    return {}


@pytest.fixture(name="delete_requests")
def delete_requests_fixture() -> list[tuple[str, dict[str, Any]]]:
    """Fixture that records DELETE requests made to the mock server."""
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
    responses: dict[str, Any],
    post_requests: list[tuple[str, dict[str, Any], dict[str, Any]]],
    post_responses: dict[str, Any],
    delete_requests: list[tuple[str, dict[str, Any]]],
    delete_responses: dict[str, Any],
) -> web.Application:
    async def handler(request: web.Request) -> web.Response:
        _LOGGER.debug("Received request: %s %s", request.method, request.path)
        requests.append((request.path, _query_string_dict(request.query_string)))
        if request.path in responses:
            return web.json_response(responses[request.path])
        return web.Response(status=404)

    async def post_handler(request: web.Request) -> web.Response:
        _LOGGER.debug("Received request: %s %s", request.method, request.path)
        body = await request.json() if request.can_read_body else {}
        post_requests.append(
            (request.path, _query_string_dict(request.query_string), body)
        )
        if request.path in post_responses:
            return web.json_response(post_responses[request.path])
        return web.Response(status=404)

    async def delete_handler(request: web.Request) -> web.Response:
        _LOGGER.debug("Received request: %s %s", request.method, request.path)
        delete_requests.append((request.path, _query_string_dict(request.query_string)))
        if request.path in delete_responses:
            return web.json_response(delete_responses[request.path])
        return web.Response(status=404)

    app = web.Application()
    app.router.add_get("/{tail:.*}", handler)
    app.router.add_post("/{tail:.*}", post_handler)
    app.router.add_delete("/{tail:.*}", delete_handler)
    return app


@pytest.fixture
async def fitbit_server(aiohttp_server: Any, fitbit_app: web.Application) -> TestServer:
    return await aiohttp_server(fitbit_app)


@pytest.fixture(name="client_session")
async def client_session_fixture(
    fitbit_server: TestServer,
    aiohttp_client: Callable[[TestServer], Awaitable[TestClient]],
) -> fitbit_web_api.ApiClient:
    """Fixture to provide an aiohttp ClientSession pointing to the test server."""
    client = await aiohttp_client(fitbit_server)
    orig_request = client.request

    # The fitbit client uses kwags with a url parameter, which is correct. However
    # the aiohttp test client uses a path parameter. So we need to adjust the
    # request to convert the url to a path.
    async def path_fix_client_request(
        method: str, url: str, **kwargs: Any
    ) -> Awaitable[web.Response]:
        path = url[len(TEST_HOST) :]
        return await orig_request(method, path=path, **kwargs)

    client.request = path_fix_client_request
    return client


@pytest.fixture
async def api_client(
    fitbit_server: TestServer,
    client_session: aiohttp.ClientSession,
) -> AsyncGenerator[fitbit_web_api.ApiClient, None]:
    configuration = fitbit_web_api.Configuration(
        pool_manager=client_session,
    )
    async with fitbit_web_api.ApiClient(configuration) as api_client:
        yield api_client


@pytest.fixture
def load_test_data() -> Callable[[str], Any]:
    """Fixture to load test data from JSON files."""

    def _load(filename: str) -> Any:
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "testdata", filename)
        with open(file_path) as f:
            return json.load(f)

    return _load
