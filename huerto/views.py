from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Count
from .models import Cultivo, Sector

class CultivoListView(ListView):
    model = Cultivo
    template_name = "huerto/cultivo_list.html"
    context_object_name = "cultivos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega al contexto la lista de sectores con la cantidad de cultivos en cada uno
        context['sectores'] = Sector.objects.all().annotate(num_cultivos=Count('cultivos'))
        return context

class CultivoCreateView(CreateView):
    model = Cultivo
    fields = ["nombre", "fecha_siembra", "estado", "sector"]
    template_name = "huerto/cultivo_form.html"
    success_url = reverse_lazy("cultivos:lista")

class CultivoUpdateView(UpdateView):
    model = Cultivo
    fields = ["nombre", "fecha_siembra", "estado", "sector"]
    template_name = "huerto/cultivo_form.html"
    success_url = reverse_lazy("cultivos:lista")

class CultivoDeleteView(DeleteView):
    model = Cultivo
    template_name = "huerto/cultivo_confirmar_eliminar.html"
    success_url = reverse_lazy("cultivos:lista")
