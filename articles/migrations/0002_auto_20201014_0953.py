# Generated by Django 3.1.2 on 2020-10-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=120)),
                ('date', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('role', models.CharField(max_length=120)),
                ('organisation', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]