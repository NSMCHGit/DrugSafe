# Generated by Django 3.0.8 on 2021-06-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_document_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='safedrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drugname', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
