from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import HomePageView, ServicePageView, ProjectsDetailView, ProjectsPageView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path(_('services/'), ServicePageView.as_view(), name='service'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('projects-in/', ProjectsDetailView.as_view(), name='projects-in'),

]
