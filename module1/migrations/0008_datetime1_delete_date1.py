# Generated by Django 4.1 on 2023-03-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0007_rename_date2_date1'),
    ]

    operations = [
        migrations.CreateModel(
            name='datetime1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time12', models.TextField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='date1',
        ),
    ]
