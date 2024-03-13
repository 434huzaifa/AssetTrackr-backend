from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class CompanyView(APIView):
    def post(self,request,format=None):
        
        return Response("post",status=201)
