# Generated by Django 4.0.4 on 2022-05-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mentord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Fullname of mentor')),
                ('subject', models.CharField(max_length=100)),
                ('experiance', models.CharField(choices=[('1', '1 year'), ('2', '2 year'), ('3', '3 year'), ('+4', 'More than 4 year')], max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.EmailField(help_text='The email id should contain @', max_length=254, null=True)),
            ],
        ),
    ]
