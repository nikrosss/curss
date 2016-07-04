from django.db import models

from django.contrib.auth.models import User



# Create your models here.

class my_work(models.Model):
    company_name = models.CharField(verbose_name = 'организация', max_length=32)
    link = models.CharField(verbose_name = 'ссылка на сайт', max_length=32)
    my_duties = models.TextField(verbose_name = 'должностные обязательства')
    periods = models.PositiveIntegerField(verbose_name = 'период работы', default = 1)


#    def __str__(self):
#        return '%s %s' % (self.company_name, self.my_duties)
