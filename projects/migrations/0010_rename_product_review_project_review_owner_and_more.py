# Generated by Django 5.0.3 on 2024-04-24 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_image'),
        ('users', '0007_rename_social_profile_social_github'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product',
            new_name='project',
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
