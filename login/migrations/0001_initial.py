# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number_1', models.CharField(max_length=50, blank=True)),
                ('mobile_number_2', models.CharField(max_length=50, blank=True)),
                ('mobile_number_3', models.CharField(max_length=50, blank=True)),
                ('mobile_number_4', models.CharField(max_length=50, blank=True)),
                ('mobile_number_5', models.CharField(max_length=50, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
