# Generated by Django 2.0.5 on 2018-05-11 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180511_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('email', models.EmailField(default='XXX@example.com', max_length=254, verbose_name='email address')),
                ('password', models.CharField(max_length=20)),
                ('phone_num', models.CharField(max_length=12, unique=True)),
                ('age', models.IntegerField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
