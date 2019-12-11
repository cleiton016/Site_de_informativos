# Generated by Django 2.2.7 on 2019-12-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informativo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informativos',
            options={'ordering': ['-data'], 'verbose_name': 'Informativo', 'verbose_name_plural': 'Informativos'},
        ),
        migrations.AddField(
            model_name='informativos',
            name='nome',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='nome'),
        ),
    ]