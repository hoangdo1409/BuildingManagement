from CompanyManagement.models import *
import datetime 
from datetime import timedelta

def ExportSalaryPaper():
    all_staff = Staff.objects.all()
    crr_month_year = datetime.datetime.now()
    str_month_year = crr_month_year.strftime("%m/%Y")
    str_month_year = str_month_year.replace("/", "")
    for stafff in all_staff:
        salary_paper_staff_by_month = SalaryPaper()
        # # salary_template_all = SalaryTemplate.objects.all()
        salary_template = list(SalaryTemplate.objects.filter(title=stafff.title))
        print(stafff.title)
        print(salary_template.salary)
        print(type(salary_template))
        salary_paper_staff_by_month.name = f"Phiếu lương của {stafff.name}"
        salary_paper_staff_by_month.code = f"SP-{stafff.code}-{str_month_year}"
        salary_paper_staff_by_month.salary = f"{salary_template.salary}"
        salary_paper_staff_by_month.salary_kpi = f"{salary_template.salary_kpi}"
        salary_paper_staff_by_month.tax = f"{stafff.tax_code}"
        salary_paper_staff_by_month.bhxh = "Chưa có"
        salary_paper_staff_by_month.total_salary = stafff.get_all_salary_by_period()
        salary_paper_staff_by_month.company = stafff.company
        salary_paper_staff_by_month.staff = stafff
        salary_paper_staff_by_month.salary_template = stafff.salary_template
        # salary_paper_staff_by_month.save() 
        print("Hello2")