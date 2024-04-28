# Generated by Django 4.2.11 on 2024-04-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_new_combrate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='my_new_combrate',
            name='supporters',
            field=models.ManyToManyField(related_name='supported_my_new_combrate', to='my_new_combrate.supporter'),
        ),
    ]
