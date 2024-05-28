# Generated by Django 3.2.4 on 2023-09-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_mytask'),
    ]

    operations = [
        migrations.CreateModel(
            name='submittedtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('answer_file', models.CharField(max_length=200, null=True)),
                ('tid', models.CharField(max_length=20, null=True)),
                ('userid', models.CharField(max_length=200, null=True)),
                ('marks', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
