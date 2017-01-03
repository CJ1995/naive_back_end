from aiohttp import web
from aiohttp.web import json_response


async def index(request):
    a = {1: 2, 2: 3}
    return json_response(a)

async def post(request):
    data = await request.post()
    print(type(data))
    # print(data['some'])
    return web.Response(text='2333')
