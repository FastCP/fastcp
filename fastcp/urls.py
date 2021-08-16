from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('dashboard/', include('core.urls', namespace='core')),
    path('', RedirectView.as_view(pattern_name='spa', permanent=False)),
    re_path(r'^dashboard/.*$', login_required(TemplateView.as_view(template_name='master.html')), name='spa')
]

urlpatterns += staticfiles_urlpatterns()