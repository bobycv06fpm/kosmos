# Generated by Django 3.0.6 on 2020-08-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kosmos', '0007_auto_20200730_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeupbag',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='makeupproduct',
            name='product_type',
            field=models.CharField(choices=[('blush', 'Blush'), ('bronzer', 'Bronzer'), ('eyebrow', 'Eyebrow'), ('eyeliner', 'Eyeliner'), ('eyeshadow', 'Eyeshadow'), ('foundation', 'Foundation'), ('lip', 'Lip Product'), ('mascara', 'Mascara'), ('nail_polish', 'Nail Polish')], max_length=32),
        ),
    ]
