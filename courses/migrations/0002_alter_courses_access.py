# Generated by Django 5.1.2 on 2024-10-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='access',
            field=models.CharField(choices=[('any', 'Anyone'), ('email_required', 'Email_Required')], default='email_required', max_length=14),
        ),
    ]
