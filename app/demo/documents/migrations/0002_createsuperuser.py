from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import migrations


def createsuperuser(apps, schema_editor):
    User = get_user_model()
    User.objects.get_or_create(
        email='test@test.com', is_superuser=True, is_active=True, is_staff=True,
        username='admin', password=make_password('123qaz123!A')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(createsuperuser, reverse_code=migrations.RunPython.noop),
    ]
