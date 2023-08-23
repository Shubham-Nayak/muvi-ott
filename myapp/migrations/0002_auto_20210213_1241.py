# Generated by Django 3.0.5 on 2021-02-13 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblcontentmaster',
            name='image_url',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='tblcontentmaster',
            name='type',
            field=models.ForeignKey(blank=True, default='NA', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Tbltypemaster'),
        ),
        migrations.AlterField(
            model_name='tblcontentmaster',
            name='video',
            field=models.FileField(upload_to=''),
        ),
    ]