# Generated by Django 3.2.5 on 2021-07-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0005_auto_20210726_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='MEDIA_COMPANY_IMAGE_DIR/bnr-1.png', height_field='height_field', upload_to='company_images', width_field='width_field'),
        ),
    ]
