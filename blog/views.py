from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Post, Device, Resource

post_list = ListView.as_view(model=Post)
post_detail = DetailView.as_view(model=Post)

class ResourceListView(ListView):
    model = Resource

    def get_queryset(self):
        self.device = get_object_or_404(Device, id=self.kwargs['device_id'])
        print(self.device)
        return Resource.objects.filter(device=self.device)

    def get_template_names(self):
        if not self.request.is_ajax():
            return ['blog/resource_list.html']
        
        return ['blog/_resource_list.html']

resource_list = ResourceListView.as_view()