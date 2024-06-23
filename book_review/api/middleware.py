

def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Headers"] = "Authorization, Content-Type, x-csrftoken"
        response["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS, PATCH"
        response["Cache-Control"] = "private, max-age=1"
        print(response)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware