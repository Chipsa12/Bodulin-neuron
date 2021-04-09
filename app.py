from aiohttp import web
import aiohttp_cors

from application.modules.image.Image import Image


# from application.modules.neuron.definitionPeopleInGroup import definitionPeople

async def getImagesHandler(request):
    post = await request.json()
    images = post.get("images")
    response = []
    for image in images:
        print(image["name"])
        Image.decodeImage(image["name"], image["image"])
        # response.append(definitionPeople(Image.decodeImage(image["name"], image["image"])))

    return web.Response(text="Привет, Андрей!!!", content_type="text")


app = web.Application()
app.router.add_route("POST", "/api/images", getImagesHandler)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        allow_headers="*"
    )
})

for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, port=9000)
