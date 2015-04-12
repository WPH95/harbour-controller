# coding: utf-8
from django.db import models
from engine.models import Engine
from label.models import Label
from image.models import Image

class Container(models.Model):
    name = models.CharField('名称', max_length = 255)
    uid = models.CharField('id', max_length = 255, unique=True)
    command = models.CharField('指令', max_length = 255)
    port = models.CharField("端口", max_length = 255)
    engine = models.ForeignKey(Engine)
    status = models.CharField('状态', max_length = 255)
    base_label = models.ManyToManyField(Label, blank=True, related_name='container.base_label')
    image = models.ForeignKey(Image)
    create_at = models.DateTimeField('创建时间', null=True)

    class Meta:
        ordering = ('id', )

    @property
    def label(self):
        return self.base_label.all()|self.engine.inherit_label.all()|self.image.inherit_label.all()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{id}:{name}".format(id=self.uid, name=self.name)