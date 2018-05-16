from django.db import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class TypeInfo(models.Model):
    t_title = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.t_title


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=40)
    gpic = RichTextUploadingField()
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isdelete = models.BooleanField(default=False)
    gtype = models.ForeignKey(TypeInfo)
    gclick = models.IntegerField(default=0)
    gunit = models.IntegerField(default=500)
    gjianjie = models.TextField()
    gpub_date = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.gtitle
