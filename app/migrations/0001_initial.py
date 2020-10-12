# Generated by Django 2.2.16 on 2020-10-12 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('document', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('site', models.CharField(max_length=30)),
                ('Attendees', models.ManyToManyField(to='app.Attendee')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
