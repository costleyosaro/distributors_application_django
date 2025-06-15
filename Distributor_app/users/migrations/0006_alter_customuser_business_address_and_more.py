from django.db import migrations, models
from django.db.models import Count

def handle_duplicates(apps, schema_editor):
    CustomUser = apps.get_model('users', 'CustomUser')

    # Find duplicate first names
    duplicate_names = CustomUser.objects.values('first_name').annotate(name_count=Count('first_name')).filter(name_count__gt=1)

    for name_data in duplicate_names:
        first_name = name_data['first_name']
        users_with_name = list(CustomUser.objects.filter(first_name=first_name).order_by('pk'))  # Order by primary key for consistency
        for i, user in enumerate(users_with_name[1:]):  # Skip the first user
            new_first_name = f"{first_name}_{user.pk}" # Use the primary key to ensure uniqueness
            user.first_name = new_first_name
            user.save()
            
class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_firstname_customuser_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='business_address',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='other_companies',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
