# Generated by Django 3.0 on 2023-12-27 08:08

from django.db import migrations

def forwards_func(apps, schema_editor):
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    new_profiles = NewProfile.objects.all()
    if new_profiles:
        for profile in new_profiles:
            profile.delete()

    NewProfile.objects.bulk_create(
        NewProfile(
            user_id=old_profile.user.id,
            favorite_city=old_profile.favorite_city,
        ) for old_profile in OldProfile.objects.all()
    )


def reverse_func(apps, schema_editor):
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    old_profiles = OldProfile.objects.all()
    if old_profiles:
        for profile in old_profiles:
            profile.delete()

    OldProfile.objects.bulk_create(
        OldProfile(
            user_id=new_profile.user.id,
            favorite_city=new_profile.favorite_city,
        ) for new_profile in NewProfile.objects.all()
    )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]


