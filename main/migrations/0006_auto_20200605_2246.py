# Generated by Django 3.0.5 on 2020-06-06 05:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200605_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
