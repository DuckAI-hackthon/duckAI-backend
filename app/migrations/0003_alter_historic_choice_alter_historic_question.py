# Generated by Django 4.2.7 on 2023-11-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_historic_choice_alter_historic_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historic',
            name='choice',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historic',
            name='question',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
