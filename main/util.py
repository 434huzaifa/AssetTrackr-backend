from icecream import ic
from functools import wraps
from rest_framework.response import Response
def check_request_data(check_list):
    """Check data inside post request.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(viewClass, *args, **kwargs):
            post_list = list(viewClass.request.data.keys())
            notfound = list()
            for i in check_list:
                if i not in post_list:
                    notfound.append(i)
            if len(notfound) != 0:
                ic(notfound)
                return Response({"msg": "Data Missing"}, status=400)
            return view_func(viewClass, *args, **kwargs)
        return _wrapped_view
    return decorator

def check_request_params(check_list):
    """Check data inside query of request.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(viewClass, *args, **kwargs):
            post_list = list(viewClass.request.query_params.keys())
            notfound = list()
            for i in check_list:
                if i not in post_list:
                    notfound.append(i)
            if len(notfound) != 0:
                ic(notfound)
                return Response({"msg": "Query missing"}, status=400)
            return view_func(viewClass, *args, **kwargs)
        return _wrapped_view
    return decorator

def sendResponse(msg,code):
    return Response({"msg":msg},status=code)