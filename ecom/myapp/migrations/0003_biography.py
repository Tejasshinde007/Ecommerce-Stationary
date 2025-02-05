# Generated by Django 5.1.4 on 2024-12-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_storybooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50, verbose_name='Product Name')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=300, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is_Available')),
                ('pimage', models.ImageField(upload_to='images')),
                ('offer_price', models.IntegerField(default=0)),
            ],
        ),
    ]
