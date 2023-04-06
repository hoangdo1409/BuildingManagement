from django.shortcuts import render

from .models import Company
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CompanySerializer
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView


def Index(request, *args, **kwargs):
    context = {}
    # context['company_template'] = 'arrgon'
    template = loader.get_template('CompanyManagement/company_list.html')
    context = Company.objects.all()
    return HttpResponse(template.render({'context': context}, request))

def Details(request, pk, *args, **kwargs):
    context = {}
    # context['company_template'] = 'arrgon'
    template = loader.get_template('CompanyManagement/detailsCompany.html')
    context = Company.objects.filter(uuid=pk)
    return HttpResponse(template.render({'context': context}, request))


class PostDetailView(DetailView):
    model = Company
    template_name = 'CompanyManagement/detailsCompany.html'