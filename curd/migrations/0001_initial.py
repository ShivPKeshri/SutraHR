# Generated by Django 2.2.4 on 2019-08-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurdOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'In Progress'), (2, 'Completed'), (3, 'Pending')], default=1)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=True)),
            ],
        ),
    ]
