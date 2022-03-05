# Generated by Django 4.0.3 on 2022-03-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebSiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Atualizado', models.IntegerField()),
                ('IP', models.GenericIPAddressField()),
                ('Porto', models.IntegerField(blank=True, null=True)),
                ('Pais', models.CharField(max_length=100)),
                ('Velocidade', models.FloatField(max_length=100)),
                ('Conectados', models.CharField(max_length=100)),
                ('Protocolo', models.CharField(max_length=100)),
                ('Anonimato', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Info',
            },
        ),
    ]