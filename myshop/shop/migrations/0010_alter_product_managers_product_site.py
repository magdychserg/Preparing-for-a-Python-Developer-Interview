# Generated by Django 4.0.4 on 2022-06-06 12:28

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('shop', '0009_alter_category_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='site',
            field=models.ManyToManyField(null=True, to='sites.site'),
        ),
    ]