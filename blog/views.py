from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
# Create your views here.

from .models import Post, Device, Resource

post_list = ListView.as_view(model=Post)
post_detail = DetailView.as_view(model=Post)

class ResourceListView(ListView):
    model = Resource

    def get_queryset(self):
        self.device = get_object_or_404(Device, id=self.kwargs['device_id'])
        return Resource.objects.filter(device=self.device)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resource_device"] = self.device
        return context

    def get_template_names(self):
        if not self.request.is_ajax():
            return ['blog/resource_list.html']
        
        return ['blog/_resource_list.html']

resource_list = ResourceListView.as_view()

def download_resource(self, pk):
    resource = get_object_or_404(Resource, pk=pk)
    print(pk)
    filename = resource.resource.name.split('/')[-1]
    print(filename)
    response = HttpResponse(resource.resource, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response