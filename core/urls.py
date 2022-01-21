from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import AuthorsViewSet, BatchViewSet, BooksViewSet, ClientViewSet, OrderViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'author', AuthorsViewSet)
router.register(r'batch', BatchViewSet)
router.register(r'book', BooksViewSet)
router.register(r'client', ClientViewSet)
router.register(r'order', OrderViewSet)
router.register(r'cadastro_usuario', UsuarioViewSet)
from core import views

urlpatterns = [
    path('', include(router.urls)),
]