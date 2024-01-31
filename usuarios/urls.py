from django.urls import path
from .views import UsuarioListCreate
from .views import UsuarioRetrieveUpdateDestroy

urlpatterns = [
    path('', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view(), name='usuario-detail'),
    path('pdf/', UsuarioListCreate.as_view(), name='usuario-list-pdf'),

]