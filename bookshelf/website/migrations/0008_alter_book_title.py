# Generated by Django 4.2.6 on 2023-10-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_book_user_add_id_book_user_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
