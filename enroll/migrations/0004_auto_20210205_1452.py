# Generated by Django 3.1.6 on 2021-02-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20210205_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ip_address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
