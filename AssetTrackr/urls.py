
from django.contrib import admin
from django.urls import path
from main import views
from rest_framework.schemas import get_schema_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path("company/",views.CompanyView.as_view()),
    path(
        "",
        get_schema_view(title="AssertTrackr", description="APIs for AssertTrackr"),
        name="openapi-schema",
    ), # This url open up the Automatic documentation of APIs
    path("employee/",views.EmployeeView.as_view()),
    path("employee/<int:pk>/",views.EmployeeView.as_view()),
    path("device/",views.DeviceView.as_view()),
    path("device/<int:pk>/",views.DeviceView.as_view()),
     
]
