# Generated by Django 2.1.1 on 2018-09-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20180921_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='filepath',
            field=models.CharField(default=None, help_text='Where is the file stored', max_length=200),
            preserve_default=False,
        ),
    ]
