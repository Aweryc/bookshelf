# Generated by Django 4.2.6 on 2023-10-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_comment_book_id_remove_comment_user_add_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]