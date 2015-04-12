# coding: utf-8
from django.db import models


class Label(models.Model):
    key = models.CharField('关键词', max_length = 255)
    value = models.CharField('值', max_length = 255)


    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'%s=%s'%(self.key, self.value)