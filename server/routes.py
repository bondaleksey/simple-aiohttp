from views import index, handle_healthcheck, handle_posthash


def setup_routes(app):
    app.router.add_get("/", index)
    app.router.add_get("/healthcheck", handle_healthcheck)
    app.router.add_post("/hash", handle_posthash)
