from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from core.models import Post, Category, Header, Service, AboutUs, SocialNetwork, CallBack, Projects, SubscribeNews, News
from django.views.generic import ListView, CreateView, TemplateView, DetailView, FormView
from django.utils import translation
from django.conf import settings
from .forms import SubscribeForm, CallBackForm


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["header"] = Header.objects.order_by('-id').first()
        context["post"] = Post.objects.all().first()
        context["category"] = Category.objects.all()
        context["projects"] = Projects.objects.all()
        context["news"] = News.objects.all()
        return context


def subform(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        print(name, email)
    return render(request, 'index.html')


class ServicePageView(ListView):
    model = Service
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = Header.objects.order_by('-id').first()
        context["services"] = Service.objects.all()

        return context


def About(request):
    context = {'about': AboutUs.objects.last()}
    return render(request, context)


class ProjectsPageView(ListView):
    model = Projects
    template_name = 'projects.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["projects"] = Projects.objects.all()
        context["header"] = Header.objects.order_by('-id').first()

        return context


class ProjectsDetailView(DetailView):
    model = Projects
    template_name = 'projects-in.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["project-in"] = Projects.objects.all()
        context['header'] = Header.objects.order_by('-id').first()

        return context


def selectlanguage(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
