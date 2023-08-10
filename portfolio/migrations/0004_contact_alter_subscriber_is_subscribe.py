# Generated by Django 4.1 on 2023-08-05 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=400)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='is_subscribe',
            field=models.BooleanField(default=True),
        ),
    ]