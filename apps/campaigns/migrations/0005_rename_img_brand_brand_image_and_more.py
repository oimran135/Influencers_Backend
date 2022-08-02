# Generated by Django 4.0.6 on 2022-08-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_alter_brand_img_alter_campaign_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='img',
            new_name='brand_image',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Completed', 'Completed'), ('Periodic-Break', 'PRD')], max_length=20, null=True),
        ),
    ]
