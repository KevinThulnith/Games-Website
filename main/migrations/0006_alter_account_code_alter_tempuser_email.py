# Generated by Django 4.1.7 on 2023-04-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_temppwd_tempuser_alter_account_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='code',
            field=models.IntegerField(default=840320),
        ),
        migrations.AlterField(
            model_name='tempuser',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]