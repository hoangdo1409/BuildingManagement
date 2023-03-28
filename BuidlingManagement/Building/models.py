from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
import uuid
from django.contrib.auth.models import User
# Create your models here.
from django.utils.timezone import now as djnow

class Buidling(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,help_text="Id tòa nha")
    name = models.CharField(max_length=1024,  editable=True,blank=False,null=False,default="tòa nha tại",help_text="Ten tòa nha")
    address = models.CharField(max_length=1024,  editable=True,blank=True,null=True,help_text="Địa chỉ")
    floor_count = models.CharField(max_length=1024,  editable=True,blank=True,null=True,help_text="số tầng")
    contact = models.CharField(max_length=1024,  editable=True,blank=True,null=True,help_text="Số liên hệ")
    
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
        verbose_name = _("Tòa Nhà")
        verbose_name_plural = _("Những Tòa Nhà")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("building_detail", kwargs={"pk": self.pk})
    def save(self,*args, **kwargs):
        if self.name is None:
            self.name = str(self.uuid)
        super().save(*args, **kwargs)
