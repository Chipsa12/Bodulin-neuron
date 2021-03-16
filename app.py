from aiohttp import web

from application.Router import Router

app = web.Application()
Router(app, web)

web.run_app(app, port=8080)
