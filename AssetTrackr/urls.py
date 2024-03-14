
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
    ),
    path("employee/",views.EmployeeView.as_view()),
     
]
