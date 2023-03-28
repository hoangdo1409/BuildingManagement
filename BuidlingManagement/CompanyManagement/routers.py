from rest_framework import routers
from .rest_views import CompanyViewSet
from .rest_views import StaffViewSet 
from .rest_views import SalaryTemplateViewSet
from .rest_views import UnitViewSet
from .rest_views import TitleViewSet
from .rest_views import SalaryPaperViewSet
from .rest_views import WorkDayViewSet
from .rest_views import SalaryPeriodDetailsViewSet
# Bộ định tuyến cung cấp một cách dễ dàng để tự động xác định URL conf.
company_router = routers.DefaultRouter()
company_router.register(r'list_company', CompanyViewSet)
# company_router.register(r'show_list', CompanyList)

# r'' - raw string: chuỗi nguyên bản sử dụng để xác định endpoint
staff_router = routers.DefaultRouter()
staff_router.register(r'list_staff', StaffViewSet)

salary_template = routers.DefaultRouter()
salary_template.register(r'salary_template', SalaryTemplateViewSet)

unit_router = routers.DefaultRouter()
unit_router.register(r'unit_com', UnitViewSet)

title_router = routers.DefaultRouter()
title_router.register(r'list_title', TitleViewSet)

salary_paper_router = routers.DefaultRouter()
salary_paper_router.register(r'list_salary_paper', SalaryPaperViewSet)

work_day_router = routers.DefaultRouter()
work_day_router.register(r'list_work_day', WorkDayViewSet)

salary_period_details_router = routers.DefaultRouter()
salary_period_details_router.register(r'salary_period_details', SalaryPeriodDetailsViewSet)
