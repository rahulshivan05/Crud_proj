# Generated by Django 3.1.6 on 2021-02-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210205_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ip_address',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Enter valid Email (xyz@gmail.com)', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, help_text='This is Blank Field', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(help_text='Enter your Full Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(help_text='Your password must contain at least 8 characters.', max_length=100),
        ),
    ]