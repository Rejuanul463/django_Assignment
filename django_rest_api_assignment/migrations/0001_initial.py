# Generated by Django 4.2 on 2023-04-08 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.CharField(choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=255)),
                ('friendliness', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('trainability', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('shedding_amount', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('exercise_needs', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=64)),
                ('favourite_food', models.CharField(max_length=255)),
                ('favourite_toy', models.CharField(max_length=255)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_rest_api_assignment.breed')),
            ],
        ),
    ]