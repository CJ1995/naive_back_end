from server.views import index, post


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/', post)