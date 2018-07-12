# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations,models
TAGS = [
    # (tagName,tagSlug)
    {"name":"augmented reality","slug":"augmented-reality"},
    {"name":"big data","slug":"big-data"},
    {"name": "ipython", "slug": "ipython"},
    {"name": "javascript", "slug": "javascript"},
    {"name": "jupyter", "slug": "jupyter"},
    {"name": "node.js", "slug": "node-js"},
    {"name": "php", "slug": "php"},
    {"name": "python", "slug": "python"},
    {"name": "ruby on rails", "slug": "ruby-on-rails"},
    {"name": "ruby", "slug": "ruby"},
    {"name": "zend", "slug": "zend"},
]
def add_tag_data(apps ,schema_editor):
    Tag = apps.get_model('organizer','Tag')
    for tag in TAGS:
        Tag.objects.create(name= tag['name'],slug= tag['slug'])

def remove_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer','Tag')
    for tag in TAGS:
        tagObject = Tag.objects.get(slug = tag['slug'])
        tagObject.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0007_startup_tag_field_optional'),
    ]

    operations = [
        migrations.RunPython(
            add_tag_data, remove_tag_data)
    ]
