# Generated by Django 2.2.5 on 2020-11-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_hospital', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('tipo_hospital', models.CharField(max_length=200)),
                ('conceito_hospital', models.CharField(max_length=200)),
            ],
        ),
    ]
