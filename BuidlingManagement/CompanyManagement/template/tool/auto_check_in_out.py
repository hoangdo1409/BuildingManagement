from CompanyManagement.models import *

import random
import datetime 
from datetime import timedelta

def AutoCheckInOut():
    all_staff = Staff.objects.all()
    hour_range_a_day = (3,10)
    start_date = datetime.date(2023, 3, 1)
    for staff in all_staff:
        for date in range(1,19):
            crr_hour_a_day = random.randint(3, 10)	
            crr_date = start_date + timedelta(days=date)
            print(date)
            crr_check_in_out = WorkDay()
            crr_date_str = crr_date.strftime("%d/%m/%Y")
            # date_and_time = datetime.datetime(2023, 3, date, 11, 2, 5)
            check_in_time = datetime.time(8, 30)
            check_out_time = datetime.time(8+crr_hour_a_day, 30)
            crr_check_in_out.name = f"[{staff.name}]({str(check_in_time)}-{str(check_out_time)})Chấm công ngày {crr_date_str}"
            crr_check_in_out.work_date = crr_date
            crr_check_in_out.check_in_date = check_in_time
            crr_check_in_out.check_out_date = check_out_time
            crr_check_in_out.staff = staff
            crr_check_in_out.company = staff.company
            crr_check_in_out.save()
