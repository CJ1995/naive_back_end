from server.views import index, post, table


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/', post)
    app.router.add_get('/table', table)
