from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from icecream import ic
from .models import Company
from functools import wraps
from .serializers import *
from django.db import IntegrityError
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
                return Response({"msg": "Data Missing"}, status=400)
            return view_func(viewClass, *args, **kwargs)
        return _wrapped_view
    return decorator

def check_request_params(check_list):
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

class CompanyView(APIView):
    """Use for create and login company
    """
    @check_request_data(["email", "password1"])
    def post(self, request):
        try:
            if "title" in request.data:
                company = Company(
                    email=request.data["email"],
                    title=request.data["title"],
                    password=request.data["password1"],
                )
                company.save()
                return Response({"msg": "Account Creation Successful"}, status=201)
            else:
                company = Company.objects.filter(email=request.data["email"]).first()
                if company:
                    company_json = CompanySerializer(company).data
                    return Response(
                        {"msg": "Successfully Login", "company": company_json}, status=200
                    )
                else:
                    return Response({"msg": "Account Not found"}, status=400)
        except IntegrityError as e:
            ic(e)
            return Response({"msg": "Email Already Exist"}, status=400)
        except Exception as e:
            ic(e)
            return Response({"msg": "Account Creation Failed"}, status=500)
    @check_request_params(["id"])
    def get(self,request):
        try:
            pass
        except Exception as e:
            ic(e)
            return Response({"msg": "Server Side Error"}, status=500)
        return Response({"msg": "Account Creation Failed"}, status=200)
