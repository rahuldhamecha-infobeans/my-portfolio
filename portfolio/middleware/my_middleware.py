
class MyMiddleware:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request, *args, **kwargs):
        print('Middleware called')
        response = self.get_response(request)

        user_agent = request.META.get('HTTP_USER_AGENT')
        print("####")
        print(user_agent)
        print("####")
        return response
