# Generated by Django 4.1.5 on 2023-01-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.CharField(choices=[('일반', '일반'), ('탈퇴', '탈퇴'), ('휴면', '휴면')], default='일반', max_length=16),
        ),
    ]
