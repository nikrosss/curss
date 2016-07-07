from django.db import models

from django.contrib.auth.models import User


# Create your models here


#    def __str__(self):
#        return '%s %s' % (self.company_name, self.my_duties)


class CompanyName(models.Model):
    id  = models.PositiveIntegerField(verbose_name = 'ID', primary_key=True)
    company_name = models.CharField(verbose_name='организация', max_length=32)
    link = models.URLField(verbose_name='ссылка на сайт', max_length=90)
    about_the_organization = models.TextField(verbose_name = 'коротко о компании')
    label = models.CharField(verbose_name='путь до картинки', max_length=32)


class MyWork(models.Model):
    id_company = models.ForeignKey(CompanyName, verbose_name = 'ID компании из CompanyName')
    links = models.CharField(verbose_name = 'ссылка на сайт', max_length=32)
    my_duties = models.TextField(verbose_name = 'должностные обязательства')
    periods = models.PositiveIntegerField(verbose_name = 'период работы', default = 1)