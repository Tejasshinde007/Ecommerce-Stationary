# Generated by Django 5.1.4 on 2025-01-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_sixthtotenth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50, verbose_name='Product Name')),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField(default=True, verbose_name='Is_Available')),
                ('pimage', models.ImageField(upload_to='images')),
            ],
        ),
    ]
