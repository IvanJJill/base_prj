# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('type_frame', models.IntegerField(default=1)),
                ('type_gender', models.IntegerField(default=1)),
                ('type_height', models.IntegerField(default=1)),
                ('description', models.TextField()),
                ('available', models.BinaryField()),
                ('image', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
