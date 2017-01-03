import asyncio
from aiohttp import web
from server.routes import setup_routes

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)

setup_routes(app)

web.run_app(app, host='127.0.0.1', port=5000)
