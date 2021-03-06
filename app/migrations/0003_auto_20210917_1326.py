# Generated by Django 3.2.7 on 2021-09-17 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210917_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityuser',
            name='group',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='app.UserGroup'),
        ),
        migrations.AlterField(
            model_name='universityuser',
            name='subject',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='title', to='app.subject'),
        ),
    ]
