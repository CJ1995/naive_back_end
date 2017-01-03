from aiohttp import web
from aiohttp.web import json_response


async def index(request):
    a = {1: 2, 2: 3}
    return json_response(a)


async def table(request):
    data = [{
        'date': '2016-05-03',
        'name': 'Tom',
        'address': 'No. 189, Grove St, Los Angeles',
    }, {
        'date': '2016-05-02',
        'name': 'Tom2',
        'address': 'No. 189, Grove St, Los Angeles',
    }, {
        'date': '2016-05-04',
        'name': 'Tom3',
        'address': 'No. 189, Grove St, Los Angeles',
    }, {
        'date': '2016-05-01',
        'name': 'Tom4',
        'address': 'No. 189, Grove St, Los Angeles',
    }]
    return json_response(data)


async def post(request):
    data = await request.post()
    print(type(data))
    # print(data['some'])
    return web.Response(text='2333')
