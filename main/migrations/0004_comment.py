# Generated by Django 3.0.5 on 2020-06-05 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200605_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.Answer')),
            ],
        ),
    ]