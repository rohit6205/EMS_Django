# Generated by Django 2.2.5 on 2019-09-10 12:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete='models.CASCADE', to='polls.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]