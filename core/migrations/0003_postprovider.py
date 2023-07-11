# Generated by Django 3.2 on 2023-07-11 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230704_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='providers', to=settings.AUTH_USER_MODEL)),
                ('reciever', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recievers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]