from rest_framework import viewsets
from .models import Company
from .models import Staff
from .models import SalaryTemplate
from .models import Unit
from .models import Title
from .models import SalaryPaper
from .models import WorkDay
from .models import SalaryPeriodDetails
from .serializers import CompanySerializer
from .serializers import StaffSerializer
from .serializers import SalaryTemplateSerializer
from .serializers import UnitSerializer
from .serializers import TitleSerializer
from .serializers import SalaryPaperSerializer
from .serializers import WorkDaySerializer
from .serializers import SalaryPeriodDetailsSerializer

# ViewSets define the view behavior.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    template_name = 'CompanyManagement/company_list.html'

    def get_queryset(self):
        query_set = self.queryset
        # fileter theo request user
        crr_user = self.request.user
        query_set_by_request_user = query_set.filter(created_by=crr_user).all()
        return query_set_by_request_user



class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get_queryset(self):
        query_set = self.queryset
        crr_user = self.request.user
        query_set_by_request_user = query_set.filter(created_by=crr_user).all()

        return query_set_by_request_user
    
class SalaryTemplateViewSet(viewsets.ModelViewSet):
    queryset = SalaryTemplate.objects.all()
    serializer_class = SalaryTemplateSerializer

    def get_queryset(self):
        query_set = self.queryset
        crr_user = self.request.user
        query_set_by_request_user = query_set.filter(created_by=crr_user).all()

        return query_set_by_request_user
    
class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def get_queryset(self):
        query_set = self.queryset
        crr_user = self.request.user
        query_set_by_request_user = query_set.filter(created_by=crr_user).all()

        return query_set_by_request_user
    
class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

    def get_queryset(self):
        query_set = self.queryset
        crr_user = self.request.user
        query_set_by_request_user = query_set.filter(created_by=crr_user).all()
        return query_set_by_request_user
    
class SalaryPaperViewSet(viewsets.ModelViewSet):
    queryset = SalaryPaper.objects.all()
    serializer_class = SalaryPaperSerializer

    # def get_queryset(self):
    #     query_set = self.queryset
    #     crr_user = self.request.user

    #     query_set_by_request_user = query_set.filter(created_by=crr_user).all()
    #     return query_set_by_request_user

class WorkDayViewSet(viewsets.ModelViewSet):
    queryset = WorkDay.objects.all()
    serializer_class = WorkDaySerializer

class SalaryPeriodDetailsViewSet(viewsets.ModelViewSet):
    queryset = SalaryPeriodDetails.objects.all()
    serializer_class = SalaryPeriodDetailsSerializer
