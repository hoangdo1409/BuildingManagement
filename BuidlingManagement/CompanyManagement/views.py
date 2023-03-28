from django.shortcuts import render

from .models import Company
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CompanySerializer
from django.http import HttpRequest


class CompanyList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'company_list.html'
    queryset = Company.objects.all()

    # def get(self, request):

    #     query_set = self.queryset
    #     # fileter theo request user
    #     crr_user = self.request.user
    #     query_set_by_request_user = query_set.filter(created_by=crr_user).all()
    #     return Response({'companies': query_set_by_request_user})
    #     # return render(request, 'CompanyManagement/company_list.html',query_set_by_request_user)


    def get(self, request):
        # assert isinstance(request, HttpRequest)
        query_set = self.queryset
        crr_user = self.request.user
        query_set_by_request_user = query_set.filter(created_by=crr_user).all()
        serializer_class = CompanySerializer(query_set_by_request_user, many=True)
        #datan = {"title":"Test Title"}
        context = {
                'companies':serializer_class.data,
            }
        return render(
            request,
            'company_list.html',
            context
        )