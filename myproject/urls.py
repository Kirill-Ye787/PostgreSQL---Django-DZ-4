from django.contrib import admin
from django.urls import path, include
from myapp import views   # 👈 добавить

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.company_list, name="home"),  # 👈 теперь "/" = список компаний
    path("", include("myapp.urls")),
]
