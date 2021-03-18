from aiohttp import web
import base64
import aiohttp_cors


def staticHandler(request):
    return web.FileResponse('./public/index.html')


async def getImageHandler(request):
    post = await request.json()
    images = post.get("images")
    print(request.content_type)
    print(images[0]["result"])
    return web.Response(text="Получил", content_type="text")


app = web.Application()
app.router.add_route("POST", "/api/images", getImageHandler)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            allow_headers="*"
    )
})

for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, port=9000)
