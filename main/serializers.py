from rest_framework import serializers
from .models import Company,Employee, Device,Checkout
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__' 
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields='__all__'

class CheckoutSerializer(serializers.ModelSerializer):
    class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employee
            fields = ["id","name"]

    class DeviceSerializer(serializers.ModelSerializer):
        class Meta:
            model=Device
            fields=["id","name"]
    employee = EmployeeSerializer(read_only=True)
    device = DeviceSerializer(read_only=True)
    return_date=serializers.DateField(format="%d-%m-%Y")
    checkout_date=serializers.DateField(format="%d-%m-%Y")
    promised_return=serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = Checkout
        exclude=["company"]
        