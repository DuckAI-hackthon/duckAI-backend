# Generated by Django 4.2.7 on 2023-11-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefone',
        ),
        migrations.AddField(
            model_name='usuario',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
    ]