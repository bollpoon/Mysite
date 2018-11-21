# Generated by Django 2.1.1 on 2018-11-18 11:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=250)),
                ('card', models.CharField(max_length=20)),
                ('card_pass', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='T_goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=250)),
                ('good_name', models.CharField(max_length=250)),
                ('good_id', models.CharField(max_length=250)),
                ('size', models.CharField(choices=[('s', ''), ('m', 'm'), ('l', 'l')], max_length=10)),
                ('color', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='T_user',
        ),
    ]