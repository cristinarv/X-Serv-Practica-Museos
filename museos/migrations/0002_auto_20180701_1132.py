# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('publicacion', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('color', models.CharField(max_length=64)),
                ('titulo', models.CharField(max_length=100)),
                ('tamaño', models.CharField(max_length=64)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content_User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('id_entidad', models.IntegerField(null=True)),
                ('descripcion', models.TextField(null=True)),
                ('horario', models.TextField(null=True)),
                ('transporte', models.TextField(null=True)),
                ('accesibilidad', models.IntegerField(null=True)),
                ('url', models.URLField(null=True)),
                ('direccion', models.CharField(max_length=64, null=True)),
                ('barrio', models.CharField(max_length=64, null=True)),
                ('distrito', models.CharField(max_length=64, null=True)),
                ('telefono', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Pages',
        ),
        migrations.AddField(
            model_name='content_user',
            name='museo',
            field=models.ForeignKey(to='museos.Museo'),
        ),
        migrations.AddField(
            model_name='content_user',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='museo',
            field=models.ForeignKey(to='museos.Museo'),
        ),
    ]
