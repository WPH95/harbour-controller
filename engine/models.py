# coding: utf-8
from django.db import models
from label.models import Label


class Engine(models.Model):
    name = models.CharField('名称', max_length = 255)
    host = models.CharField('地址', max_length = 255)
    port = models.IntegerField("端口", default = 0)
    token = models.CharField('Token', max_length = 255)
    base_label = models.ManyToManyField(Label, blank=True, related_name='engine.base_label')
    inherit_label = models.ManyToManyField(Label, blank=True, related_name='engine.inherit_label')

    class Meta:
        ordering = ('id', )

    @property
    def label(self):
        return self.base_label.all()

    def url(self, path='/'):
        return "http://{host}:{post}{path}?key={token}".format(host=self.host,
                                                         post=self.port,
                                                         token=self.token,
                                                         path=path)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{name}@{host}".format(host=self.host,name=self.name)