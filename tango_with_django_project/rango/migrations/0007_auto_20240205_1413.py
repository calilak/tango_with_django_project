# Generated by Django 2.2.28 on 2024-02-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_alter_category_id_alter_page_id_alter_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]