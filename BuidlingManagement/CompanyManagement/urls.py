from django.urls import path, include
from .routers import company_router 
from .routers import staff_router
from .routers import salary_template
from .routers import unit_router
from .routers import title_router 
from .routers import salary_paper_router
from .routers import work_day_router
from .routers import salary_period_details_router
from . import views
from .views import PostDetailView

urlpatterns = [
    path('company/', include(company_router.urls)),
    path('staff/', include(staff_router.urls)),
    path('salary_template/', include(salary_template.urls)),
    path('unit/', include(unit_router.urls)),
    path('title/', include(title_router.urls)),
    path('salary_paper/', include(salary_paper_router.urls)),
    path('work_day/', include(work_day_router.urls)),
    path('salary_period_details/', include(salary_period_details_router.urls)),

    path('', views.Index, name='company'),
    path('details/<uuid:pk>/', PostDetailView.as_view(), name='details'),

]