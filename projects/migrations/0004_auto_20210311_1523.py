# Generated by Django 3.1.6 on 2021-03-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210311_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/noimage.jpg', upload_to='products'),
        ),
    ]