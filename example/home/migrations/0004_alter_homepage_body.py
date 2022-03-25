# Generated by Django 4.0.3 on 2022-03-18 04:25

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_homepage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "heading",
                        wagtail.core.blocks.CharBlock(form_classname="full title"),
                    ),
                    ("paragraph", wagtail.core.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                ]
            ),
        ),
    ]
