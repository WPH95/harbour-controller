# coding: utf-8
from django.db import models
from engine.models import Engine
from label.models import Label
import json

class Image(models.Model):
    name = models.CharField('名称', max_length = 255)
    uid = models.CharField('id', max_length = 255, blank=True)
    command = models.CharField('指令', max_length = 255, blank=True)
    ip = models.IntegerField("端口", default = 0, blank=True)
    status = models.CharField('状态', max_length = 255)
    tag =  models.CharField('标签（json格式）', max_length = 255)
    order = models.IntegerField('优先度', default = 9)
    size = models.IntegerField('实际大小', default = 99)
    create_at = models.DateTimeField('创建时间')
    virtualsize = models.IntegerField('虚拟大小', default = 99)
    base_label = models.ManyToManyField(Label, blank=True, related_name='image.base_label')
    inherit_label = models.ManyToManyField(Label, blank=True, related_name='image.inherit_label')
    engine = models.ForeignKey(Engine)

    class Meta:
        ordering = ('order', )

    @property
    def label(self):
        return self.base_label.all() | self.engine.inherit_label.all()

    @property
    def tags(self):
        return json.loads(self.tag)


    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{id}:{name}".format(id=self.uid, name=self.name)