# Generated by Django 2.2.3 on 2019-07-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0006_auto_20190718_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplebot',
            name='sample_image',
            field=models.ImageField(upload_to='attach-images/%y-%m-%d_%H:%M'),
        ),
    ]
