# Generated by Django 2.0.7 on 2018-07-22 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180722_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='clinicname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('W', '원장'), ('M', '마케팅담당자'), ('S', '병원관계자')], default='M', max_length=1),
        ),
    ]
