# Generated by Django 2.0.7 on 2018-08-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180724_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='contenturl',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
