# Generated by Django 4.1 on 2022-08-26 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_useritem'),
    ]

    operations = [
        migrations.AddField(
            model_name='useritem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
