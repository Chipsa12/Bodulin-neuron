class Router:
    def __init__(self, app, web):
        self.web = web

        app.router.add_static('/js/', path=str('./public/'))

        app.add_routes([web.get('/test', self.testHandler),
                        web.post('/*', self.staticHandler)])

        print("Server is running")

    def testHandler(self, request):
        return self.web.json_response(dict(result='I\'m alive'))

    def staticHandler(self, request):
        return self.web.Response('./public/index.html')
