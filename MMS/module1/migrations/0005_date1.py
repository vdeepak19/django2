# Generated by Django 4.1 on 2023-03-02 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0004_contactus_alter_faculty_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='date1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'date1',
            },
        ),
    ]
