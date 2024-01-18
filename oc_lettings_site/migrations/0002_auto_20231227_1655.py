# Generated by Django 3.0 on 2023-12-27 16:55

from django.db import migrations


class Migration(migrations.Migration):
    """
    Pour transfert de l'app oc_lettings_site vers deux apps,
    suppression des tables oc_lettings_site.Address, oc_lettings_site.Letting
    et oc_lettings_site.Profile
    """

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letting',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
