from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid
import datetime
# import settings.user
from django.utils.timezone import now as djnow

# Chi tiết về kỳ lương


class SalaryPeriodDetails(models.Model):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False,
                            help_text="Id Don Vi"
                            )

    name = models.CharField(max_length=1024,
                            editable=True,
                            blank=False,
                            null=False,
                            default="Tên kỳ lương chi tiết",
                            help_text="Tên Kỳ lương chi tiết"
                            )

    code = models.CharField(max_length=1024,
                            editable=True,
                            blank=True,
                            null=True,
                            help_text="Mã kỳ lương chi tiết"
                            )

    created_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_created_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người tạo'
                                   )
    updated_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_updated_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người cập nhật'
                                   )
    updated_at = models.DateTimeField(
        default=djnow,
        help_text='Thời điểm cập nhật'
    )
    created_at = models.DateTimeField(
        default=djnow,
        editable=False,
        help_text='Ngày đăng tải')

    class Meta:
        verbose_name = _("Chi tiết về kỳ lương")
        verbose_name_plural = _("Những Chi tiết về kỳ lương")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)

# Thông tin về công ty

class Company(models.Model):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False,
                            help_text="Id Công Ty"
                            )

    name = models.CharField(max_length=1024,
                            editable=True,
                            blank=True,
                            null=True,
                            default="Công Ty hiện tại",
                            help_text="Tên Công Ty"
                            )

    address = models.CharField(max_length=1024,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="Địa chi"
                               )

    floor_count = models.CharField(max_length=1024,
                                   editable=True,
                                   blank=True,
                                   null=True,
                                   help_text="Tầng số"
                                   )

    member_count = models.CharField(max_length=1024,
                                    editable=True,
                                    blank=True,
                                    null=True,
                                    help_text="Số thành viên"
                                    )

    tax_code = models.CharField(max_length=1024,
                                editable=True,
                                unique=True,
                                blank=True,
                                null=True,
                                help_text="Số thành viên"
                                )

    owners = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               null=True,
                               help_text="chủ tịch"
                               )

    parent_company = models.ForeignKey('self',
                                       on_delete=models.CASCADE,
                                       blank=True,
                                       null=True,
                                       help_text="chủ tịch",
                                       )

    contact = models.CharField(max_length=1024,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="Số liên hệ"
                               )
    # period_type: Loại kỳ trả lương
    period_type = models.CharField(max_length=1024,
                                   editable=True,
                                   blank=False,
                                   null=True,
                                   help_text="Loại kỳ trả lương")

    created_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_created_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người tạo')

    updated_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_updated_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người cập nhật')
    updated_at = models.DateTimeField(default=djnow,
                                      help_text='Thời điểm cập nhật')

    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text='Ngày đăng tải')

    class Meta:
        verbose_name = _("Công Ty")
        verbose_name_plural = _("Những Công Ty")

    def __str__(self):
        return self.name

    def get_child_company(self):
        return 0
    # def get_absolute_url(self):
    #     return reverse("building_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)

class Title(models.Model):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False,
                            help_text="Id Đơn Vi")

    name = models.CharField(max_length=1024,
                            editable=True,
                            blank=False,
                            null=False,
                            default="Chức danh hiện tại",
                            help_text="Tên Chức danh")

    code = models.CharField(max_length=1024,
                            editable=True,
                            blank=True,
                            null=True,
                            help_text="Mã chức danh")

    created_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_created_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người tạo')

    updated_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_updated_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người cập nhật')

    updated_at = models.DateTimeField(default=djnow,
                                      help_text='Thời điểm cập nhật')

    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text='Ngày đăng tải')

    class Meta:
        verbose_name = _("Chức danh")
        verbose_name_plural = _("Những chức danh")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)


class Unit(models.Model):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False,
                            help_text="Id Don Vi")
    name = models.CharField(max_length=1024,
                            editable=True,
                            blank=False,
                            null=False,
                            default="Don Vi hiện tại",
                            help_text="Ten Don Vi")

    address = models.CharField(max_length=1024,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="Địa chi")

    floor_count = models.CharField(max_length=1024,
                                   editable=True,
                                   blank=True,
                                   null=True,
                                   help_text="tầng số")

    member_count = models.CharField(max_length=1024,
                                    editable=True,
                                    blank=True,
                                    null=True,
                                    help_text="Số thành viên")

    tax_code = models.CharField(max_length=1024,
                                editable=True,
                                blank=True,
                                null=True,
                                help_text="Số thành viên")

    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                help_text="chủ tịch")

    contact = models.CharField(max_length=1024,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="Số liên hệ")

    created_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_created_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người tạo')

    updated_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_updated_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người cập nhật')

    updated_at = models.DateTimeField(default=djnow,
                                      help_text='Thời điểm cập nhật')

    created_at = models.DateTimeField(
        default=djnow,
        editable=False,
        help_text='Ngày đăng tải')

    class Meta:
        verbose_name = _("Đơn vị")
        verbose_name_plural = _("Những Đơn vị")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("building_detail", kwargs={"pk": self.pk})
    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)


class SalaryTemplate(models.Model):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False,
                            help_text="Id Don Vi")

    name = models.CharField(max_length=1024,
                            editable=True,
                            blank=False,
                            null=False,
                            default="Tên Lương mẫu",
                            help_text="Tên lương mẫu")

    code = models.CharField(max_length=1024,
                            editable=True,
                            blank=True,
                            null=True,
                            help_text="Mã lương mẫu")

    salary = models.CharField(max_length=1024,
                              editable=True,
                              blank=True,
                              null=True,
                              help_text="Lương ngày công")

    salary_kpi = models.CharField(max_length=1024,
                                  editable=True,
                                  blank=True,
                                  null=True,
                                  help_text="Lương KPI")

    title = models.ForeignKey(Title,
                            on_delete=models.SET_NULL,
                            null=True,
                            help_text="Chức danh"
                            )

    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                help_text="Chủ tịch")
    # company (Chủ tịch)
    created_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_created_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người tạo')

    updated_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_updated_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người cập nhật')

    updated_at = models.DateTimeField(default=djnow,
                                      help_text='Thời điểm cập nhật')

    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text='Ngày đăng tải')

    class Meta:
        verbose_name = _("Cơ cấu lương mẫu")
        verbose_name_plural = _("Những Cơ cấu lương mẫu")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("building_detail", kwargs={"pk": self.pk})
    def save(self, *args, **kwargs):

        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)


class Staff(models.Model):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False,
                            help_text="Id Don Vi")

    name = models.CharField(max_length=1024,
                            editable=True,
                            blank=False,
                            null=False,
                            default="Nhân viên",
                            help_text="Tên nhân viên")

    code = models.CharField(max_length=1024,
                            editable=True,
                            blank=True,
                            null=True,
                            help_text="Mã nhân viên")

    address = models.CharField(max_length=1024,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="Địa chi")

    id_code = models.CharField(max_length=1024,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="CCCD")

    tax_code = models.CharField(max_length=1024,
                                editable=True,
                                blank=True,
                                null=True,
                                help_text="Mã số thuế")

    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                null=True,
                                help_text="Chủ tịch")

    unit = models.ForeignKey(Unit,
                             on_delete=models.SET_NULL,
                             null=True,
                             help_text="Thuộc đơn vị"
                             )

    salary_template = models.ForeignKey(SalaryTemplate,
                                        on_delete=models.CASCADE,
                                        help_text="Cơ cấu lương")
    # unit (Thuộc đơn vị)
    # salary_template (Cơ cấu lương)
    title = models.ForeignKey(Title,
                              on_delete=models.SET_NULL,
                              null=True,
                              help_text="Chức danh"
                              )

    contact = models.CharField(max_length=1024,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="Số liên hệ")

    created_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_created_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người tạo')

    updated_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_updated_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người cập nhật')

    updated_at = models.DateTimeField(default=djnow,
                                      help_text='Thời điểm cập nhật')

    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text='Ngày đăng tải')

    class Meta:
        verbose_name = _("Nhân viên")
        verbose_name_plural = _("Những nhân viên")

    def __str__(self):
        return self.name
     # Lấy dữ liệu ngày công theo kỳ

    # lấy dữ liệu ngày công theo kỳ
    def get_all_work_day_by_period(self):
        all_work_days_count = 0
        if self.company.period_type == "month":
            crr_month = datetime.datetime.today().month
            all_work_days = WorkDay.objects.filter(
                staff=self, work_date__month=crr_month).all()
            all_work_days_count = all_work_days.count()

        return all_work_days_count  # lấy dữ liệu ngày công theo kỳ

    def get_all_salary_work_day_by_period(self):
        all_work_days_count = 0
        if self.company.period_type == "month":
            crr_month = datetime.datetime.today().month
            all_work_days = WorkDay.objects.filter(
                staff=self, work_date__month=crr_month).all()
            crr_work_day_sum = 0
            for day in all_work_days:
                crr_work_hours = 0
                try:
                    crr_work_day = 0
                    # work_diff = (day.check_out_date - day.check_in_date)
                    # Create datetime objects for each time (a and b)
                    dateTimeA = datetime.datetime.combine(
                        datetime.date.today(), day.check_out_date)
                    dateTimeB = datetime.datetime.combine(
                        datetime.date.today(), day.check_in_date)
                    # Get the difference between datetimes (as timedelta)
                    dateTimeDifference = dateTimeA - dateTimeB
                    # Divide difference in seconds by number of seconds in hour (3600)
                    work_hours = dateTimeDifference.total_seconds() / 3600
                    # work_hours = work_diff.seconds / 3600
                    # work_hours = datetime.datetime.combine(datetime.datetime.today(), day.check_out_date) - datetime.combine(datetime.datetime.today(), day.check_in_date).hours
                    if work_hours >= 8:
                        crr_work_day = 1
                    elif work_hours >= 4:
                        crr_work_day = 0.5
                    crr_work_day_sum += crr_work_day
                except Exception as xx:
                    print("err when count hour work a day %s" % str(xx))

            # all_work_days_count = all_work_days.count()

        return crr_work_day_sum

    def get_all_salary_by_period(self):
        crr_salary = 0
        crr_salary_day = self.get_all_salary_work_day_by_period()
        if crr_salary_day > 0 and self.salary_template:
            crr_salary = float(
                crr_salary_day) * (float(self.salary_template.salary)+float(self.salary_template.salary_kpi))
            crr_tax = 0
            if crr_salary > 0:
                crr_tax = crr_salary * 0.105
            crr_salary = crr_salary - crr_tax
            pass
        return crr_salary

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)

# chức danh


class SalaryPaper(models.Model):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False,
                            help_text="Id Don Vi"
                            )

    name = models.CharField(max_length=1024,
                            editable=True,
                            blank=True,
                            null=False,
                            default="Tên phiếu lương theo từng nhân viên",
                            help_text="Tên phiếu lương theo từng nhân viên"
                            )

    code = models.CharField(max_length=1024,
                            editable=True,
                            blank=True,
                            null=True,
                            help_text="Mã Phiếu lương theo từng nhân viên")
    salary = models.CharField(max_length=1024,
                              editable=True,
                              blank=True,
                              null=True,
                              help_text="Lương ngày công")
    salary_kpi = models.CharField(max_length=1024,
                                  editable=True,
                                  blank=True,
                                  null=True,
                                  help_text="Lương KPI")

    tax = models.CharField(max_length=1024,
                           editable=True,
                           blank=True,
                           null=True,
                           help_text="Thuế")

    bhxh = models.CharField(max_length=1024,
                            editable=True,
                            blank=True,
                            null=True,
                            help_text="Bảo hiểm xã hội")

    total_salary = models.CharField(max_length=1024,
                                    editable=True,
                                    blank=True,
                                    null=True,
                                    help_text="Tổng lương")

    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                help_text="Công ty")

    staff = models.ForeignKey(Staff,
                              on_delete=models.SET_NULL,
                              null=True,
                              help_text="Nhân viên")

    salary_template = models.ForeignKey(SalaryTemplate,
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        help_text="Cơ cấu lương mẫu")

    period = models.ForeignKey(SalaryPeriodDetails,
                               on_delete=models.SET_NULL,
                               null=True,
                               help_text="Kỳ trả lương")

    # bhxh, total_salary, day_work, company
    # staff(Fk(Staff)), salary_template(FK(SalaryTemplate)), period(FK(SalaryPeriodDetails)),

    created_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_created_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người tạo')

    updated_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_updated_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người cập nhật')

    updated_at = models.DateTimeField(default=djnow,
                                      help_text='Thời điểm cập nhật')

    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text='Ngày đăng tải')

    class Meta:
        verbose_name = _("Phiếu lương theo từng nhân viên")
        verbose_name_plural = _("Các phiếu lương theo từng nhân viên")

    def __str__(self):
        return self.name
    # Lấy dữ liệu ngày công theo kỳ

    def get_all_work_day_by_period(self):
        all_work_by_period = WorkDay.objects.filter(
            staff=self.staff.uuid).all()
        return all_work_by_period

    # def export_salary_paper_by_period(self):
    #     all_staff = Staff.objects.all()
    #     crr_month_year = datetime.datetime.now()
    #     str_month_year = crr_month_year.strftime("%m/%Y")
    #     str_month_year = str_month_year.replace("/", "")

    #     for staff in all_staff:
    #         salary_paper_staff_by_month = SalaryPaper()
    #         salary_template = SalaryTemplate()
    #         salary_paper_staff_by_month.name = f"Phiếu lương của {staff.name}"
    #         salary_paper_staff_by_month.code = f"SP-{staff.code}-{str_month_year}"
    #         salary_paper_staff_by_month.salary = f"{salary_template.salary}"
    #         salary_paper_staff_by_month.salary_kpi = f"{salary_template.salary_kpi}"
    #         salary_paper_staff_by_month.tax = f"{staff.tax_code}"
    #         salary_paper_staff_by_month.bhxh = "Chưa có"
    #         salary_paper_staff_by_month.total_salary = staff.get_all_salary_by_period()
    #         salary_paper_staff_by_month.company = staff.company
    #         salary_paper_staff_by_month.staff = staff.name

    #         for salary_temp in salary_template:
    #             if staff.title == salary_temp.title:
    #                 salary_paper_staff_by_month.salary_template == salary_temp.name
    #         salary_template.save()

    def save(self, *args, **kwargs):

        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)

# Khi mà xóa thì dặt là ....


class WorkDay(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False,
                            help_text="Id Don Vi")
    name = models.CharField(max_length=1024,  editable=True, blank=False,
                            null=False, default="Ngày làm việc", help_text="Ten Chức danh")
    code = models.CharField(max_length=1024,  editable=True,
                            blank=True, null=True, help_text="Mã chức danh")

    staff = models.ForeignKey(Staff,
                              on_delete=models.CASCADE,
                              help_text="Nhân viên ")

    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                help_text="Công ty")

    # staff(Fk(Staff)), company(fk(Company))

    work_date = models.DateField(default=djnow,
                                 help_text="Ngày làm việc")

    check_in_date = models.TimeField(default=djnow,
                                     help_text="Thời điểm checkin")

    check_out_date = models.TimeField(default=djnow,
                                      help_text="Thời điểm check out")

    # work_date, check_in_date, check_out_date.
    created_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_created_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người tạo')

    updated_by = models.ForeignKey(User,
                                   to_field='username',
                                   related_name='%(class)s_updated_by',
                                   on_delete=(models.SET_NULL),
                                   null=True,
                                   blank=True,
                                   help_text='Người cập nhật')

    updated_at = models.DateTimeField(default=djnow,
                                      help_text='Thời điểm cập nhật')
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text='Ngày đăng tải')

    class Meta:
        verbose_name = _("Ngày công theo nhân viên")
        verbose_name_plural = _("Những ngày công theo nhân viên")

    def __str__(self):
        return self.name
    # Lấy dữ liệu ngày công theo kỳ

    def get_all_work_day_by_period(self):
        pass

    def save(self, *args, **kwargs):

        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)
