from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from core.views import Logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view())
]
