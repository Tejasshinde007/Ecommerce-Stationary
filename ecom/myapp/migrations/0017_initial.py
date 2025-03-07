# Generated by Django 5.1.4 on 2025-01-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0016_delete_biography_remove_cart_pid_remove_cart_userid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50, verbose_name='Product Name')),
                ('price', models.IntegerField()),
                ('category', models.IntegerField(choices=[(1, 'Storybooks'), (2, 'Biography'), (3, 'Lkg1'), (4, 'Firsttofifth'), (5, 'Sixthtotenth'), (6, 'Writting Instruments')], verbose_name='Category')),
                ('description', models.CharField(max_length=300, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is_Available')),
                ('pimage', models.ImageField(upload_to='images')),
                ('offer_price', models.IntegerField(default=0)),
            ],
        ),
    ]
