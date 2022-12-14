# Generated by Django 3.1.14 on 2022-11-24 14:38

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=500, unique=True)),
                ('category_selector', models.CharField(max_length=500)),
                ('subcategory_selector', models.CharField(max_length=500)),
                ('title_selector', models.CharField(max_length=500)),
                ('price_selector', models.CharField(max_length=500)),
                ('currency_selector', models.CharField(max_length=500)),
                ('summary_selector', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
