# Generated by Django 3.0.4 on 2021-03-13 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20210310_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi departamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
    ]
