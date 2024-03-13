from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from icecream import ic
from .models import Company
from functools import wraps
# Create your views here.
def check_request_data(check_list):
    """Check data inside post request. then print data if any given key/name missing. then return accoridingly
    Parameters
    ----------
    request_post : QueryDict/Dict
        request.POST will be here
    check_list : list 
        List of names/key should be inside request.POST

    Returns
    -------
    bool
        if everyitem is not found then it will return false, otherwise true
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
                return Response({"msg": "Key Missing"}, status=400)
            return view_func(viewClass, *args, **kwargs)
        return _wrapped_view
    return decorator
class CompanyView(APIView):
    @check_request_data(["email","title","password1"])
    def post(self,request):
        try:
            company=Company(email=request.data["email"],title=request.data['title'],password=request.data['password1'])
            company.save()
            return Response({"msg":"Account Creation Successful"},status=201)
        except Exception as e:  
            ic(e)
            return Response({"msg":"Account Creation Failed"},status=400)
