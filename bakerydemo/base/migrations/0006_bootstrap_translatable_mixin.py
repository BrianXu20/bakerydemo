# Generated by Django 3.1.6 on 2021-02-26 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('base', '0005_formfield_clean_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='footertext',
            name='locale',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
        ),
        migrations.AddField(
            model_name='footertext',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='locale',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
        ),
        migrations.AddField(
            model_name='people',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
