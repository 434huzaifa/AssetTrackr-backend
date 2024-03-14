from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from icecream import ic
from .models import Company, Employee,Device
from .util import *
from .serializers import *
from django.db import IntegrityError

# Create your views here.


class CompanyView(APIView):
    @check_request_data(["email", "password1"])
    def post(self, request):
        """Use for create and login company"""
        try:
            if "title" in request.data:
                company = Company(
                    email=request.data["email"],
                    title=request.data["title"],
                    password=request.data["password1"],
                )
                company.save()
                return sendResponse("Account Creation Successful", 201)
            else:
                company = Company.objects.filter(email=request.data["email"]).first()
                if company:
                    if company.password == request.data["password1"]:
                        company_json = CompanySerializer(company).data
                        return Response(
                            {"msg": "Successfully Login", "company": company_json},
                            status=200,
                        )
                    else: 
                        return sendResponse("Account Information mismatch",400)
                else:
                    
                    return sendResponse("Account Not found",400)
        except IntegrityError as e:
            ic(e)
            return sendResponse("Email Already Exist",400)
        except Exception as e:
            ic(e)
            return sendResponse("Server Side Error", 500)

    @check_request_params(["id"])
    def get(self, request):
        """Get Company email and title"""
        try:
            company = Company.objects.filter(id=request.query_params["id"]).first()
            if company:
                company_json = CompanySerializer(company)

                company_json.fields.pop("password")
                return Response(
                    {"msg": "Data Found", "company": company_json.data}, status=200
                )
            else:
                return Response({"msg": "Account Not found"}, status=400)
        except Exception as e:
            ic(e)
            return Response({"msg": "Server Side Error"}, status=500)


class EmployeeView(APIView):
    @check_request_data(["company", "name", "delegate"])
    def post(self, request):
        """Insert employee information"""
        try:
            company = Company.objects.filter(id=request.data["company"]).first()
            if company:
                emp = Employee(
                    company=company,
                    name=request.data["name"],
                    delegate=request.data["delegate"],
                )
                emp.save()
                return sendResponse("Employee Created", 201)
            else:
                return sendResponse("Company not found", 400)
        except Exception as e:
            ic(e)
            return sendResponse("Server Side Error", 500)
    @check_request_params(["id"])
    def get(self,request):
        """Get al the employee information of the company
        """
        try:
            emp=Employee.objects.filter(company_id=request.query_params["id"])
            emp=EmployeeSerializer(emp,many=True)
            return Response({"msg":"Success","employees":emp.data},status=200)
        except Exception as e:
            ic(e)
            return sendResponse("Server Side Error",500)
    def delete(self,request,pk):
        """Delete Employee with their id
        """
        try:
            emp=Employee.objects.filter(id=pk).first()
            emp.delete()
            return sendResponse("Deleted Successfully",200)
        except Exception as e:
            ic(e)
            return sendResponse("Server Side Error",500)

class DeviceView(APIView):
    @check_request_data(["condition","company","name"])
    def post(self,request):
        """Insert Device Information
        """
        try:
            company = Company.objects.filter(id=request.data["company"]).first()
            if company:
                device= Device(name=request.data['name'],company=company,condition=request.data['condition'])
                device.save()
                return sendResponse("Device Created", 201)
            else:
                return sendResponse("Company not found", 400)
        except Exception as e:
            ic(e)
            return sendResponse("Server Side Error",500)
    @check_request_params(['id'])
    def get(self,request):
        """_summary_
        """
        try:
            device=Device.objects.filter(company_id=request.query_params['id'])
            device=DeviceSerializer(device,many=True)
            return Response({"msg":"Success","devices":device.data},status=200)
        except Exception as e:
            ic(e)
            return sendResponse("Server Side Error",500)