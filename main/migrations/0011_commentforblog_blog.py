# Generated by Django 4.2.7 on 2023-11-07 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_commentforblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentforblog',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.blogs'),
        ),
    ]
