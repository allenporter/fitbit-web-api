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


@pytest.fixture
def responses() -> Dict[str, Any]:
    return {}


@pytest.fixture
async def fitbit_app(responses: Dict[str, Any]) -> web.Application:
    async def handler(request: web.Request) -> web.Response:
        if request.path in responses:
            return web.json_response(responses[request.path])
        return web.Response(status=404)

    app = web.Application()
    app.router.add_get("/{tail:.*}", handler)
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
