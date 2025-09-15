from django.urls import path
from . import views

app_name = "cultivos"

urlpatterns = [
    path('', views.CultivoListView.as_view(), name="lista"),
    path('nuevo/', views.CultivoCreateView.as_view(), name="crear"),
    path('<int:pk>/editar/', views.CultivoUpdateView.as_view(), name="editar"),
    path('<int:pk>/eliminar/', views.CultivoDeleteView.as_view(), name="eliminar"),
]
