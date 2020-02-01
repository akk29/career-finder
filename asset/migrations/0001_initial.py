# Generated by Django 3.0.2 on 2020-02-01 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registeration', '0002_auto_20200201_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=150)),
                ('createBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registeration.UserProfile')),
            ],
        ),
    ]
