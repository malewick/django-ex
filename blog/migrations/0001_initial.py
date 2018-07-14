# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=140)),
                ('short', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('datefrom', models.DateField(blank=True, null=True)),
                ('dateto', models.DateField(blank=True, null=True)),
                ('place', models.CharField(max_length=140, blank=True, null=True)),
                ('link1', models.URLField(blank=True, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
                ('link3', models.URLField(blank=True, null=True)),
                ('tag1', models.CharField(max_length=240, blank=True, choices=[('conference', 'conference'), ('popularization', 'popularization'), ('award', 'award'), ('collaboration', 'collaboration'), ('organization', 'organization'), ('job', 'job'), ('project', 'project'), ('seminar', 'seminar')])),
                ('tag2', models.CharField(max_length=240, blank=True, choices=[('conference', 'conference'), ('popularization', 'popularization'), ('award', 'award'), ('collaboration', 'collaboration'), ('organization', 'organization'), ('job', 'job'), ('project', 'project'), ('seminar', 'seminar')])),
                ('tag3', models.CharField(max_length=240, blank=True, choices=[('conference', 'conference'), ('popularization', 'popularization'), ('award', 'award'), ('collaboration', 'collaboration'), ('organization', 'organization'), ('job', 'job'), ('project', 'project'), ('seminar', 'seminar')])),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='pictures')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='pictures')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='pictures')),
                ('file1', models.FileField(blank=True, null=True, upload_to='files')),
                ('file2', models.FileField(blank=True, null=True, upload_to='files')),
                ('file3', models.FileField(blank=True, null=True, upload_to='files')),
            ],
        ),
    ]
