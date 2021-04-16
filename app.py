from aiohttp import web
import aiohttp_cors
import json


from application.modules.image.Image import Image
from application.modules.neuron.definitionPeopleInGroup import definitionPeople
from application.modules.neuron_found_face_people.found_face_people_separately_face import main


async def getImagesHandler(request):
    post = await request.json()
    images = post.get("images")
    response = []
    for image in images:
        for i in image:
            img = Image.decodeImage(i["name"], i["image"])
            response.append(definitionPeople(img.binary))

    return web.json_response(response)


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

# arr = main('bodulin.jpg')

# definitionPeople('img1.jpg')

web.run_app(app, port=9000)
