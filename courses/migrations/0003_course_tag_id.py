# Generated by Django 2.2.4 on 2019-10-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20191011_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Tag_ID',
            field=models.ManyToManyField(to='courses.Tag'),
        ),
    ]
