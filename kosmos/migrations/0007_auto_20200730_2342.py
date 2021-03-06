# Generated by Django 3.0.6 on 2020-07-31 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kosmos', '0006_auto_20200728_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeupproduct',
            name='category',
            field=models.CharField(choices=[('powder', 'Powder'), ('cream', 'Cream'), ('pencil', 'Pencil'), ('liquid', 'Liquid'), ('gel', 'Gel'), ('palette', 'Palette'), ('contour', 'Contour'), ('bb_cc', 'BB/CC'), ('concealer', 'Concealer'), ('mineral', 'Mineral'), ('highlighter', 'Highlighter'), ('lipstick', 'Lipstick'), ('lip_gloss', 'Lip Gloss'), ('lip_stain', 'Lip Stain'), ('lip_liner', 'Lip Liner'), ('none', 'N/A')], max_length=16),
        ),
        migrations.AlterField(
            model_name='makeupproduct',
            name='product_type',
            field=models.CharField(choices=[('blush', 'Blush'), ('bronzer', 'Bronzer'), ('eyebrow', 'Eyebrow'), ('eyeliner', 'Eyeliner'), ('eyeshadow', 'Eyeshadow'), ('foundation', 'Foundation'), ('lip_liner', 'Lip Liner'), ('lipstick', 'Lipstick'), ('lip', 'Lip Product'), ('mascara', 'Mascara'), ('nail_polish', 'Nail Polish')], max_length=32),
        ),
    ]
