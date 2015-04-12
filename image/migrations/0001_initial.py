# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('label', '__first__'),
        ('engine', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('uid', models.CharField(max_length=255, verbose_name=b'id')),
                ('command', models.CharField(max_length=255, verbose_name=b'\xe6\x8c\x87\xe4\xbb\xa4')),
                ('ip', models.IntegerField(default=0, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3')),
                ('status', models.CharField(max_length=255, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('tag', models.CharField(max_length=255, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xef\xbc\x88json\xe6\xa0\xbc\xe5\xbc\x8f\xef\xbc\x89')),
                ('order', models.IntegerField(default=99, verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe5\xba\xa6')),
                ('size', models.IntegerField(default=99, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('create_at', models.DateTimeField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('virtualsize', models.IntegerField(default=99, verbose_name=b'\xe8\x99\x9a\xe6\x8b\x9f\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('base_label', models.ManyToManyField(related_name='image.base_label', to='label.Label', blank=True)),
                ('engine', models.ForeignKey(to='engine.Engine')),
                ('inherit_label', models.ManyToManyField(related_name='image.inherit_label', to='label.Label', blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
    ]
