# Generated by Django 3.0.5 on 2020-04-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
