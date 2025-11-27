The Django Template Language (DTL) is a built-in templating system for the Django web framework, enabling dynamic HTML (or
other text formats) generation by embedding variables, tags, filters, and comments within static templates.[1][4]

## Key Components

DTL uses `{{ variable }}` syntax to insert context values from views, such as `{{ section.title }}` replacing with an
object's attribute. Tags like `{% for %}` and `{% if %}` handle logic, such as looping over lists
(`{% for story in story_list %}`) or conditionals, while filters modify output (e.g.,(e.g.,
`{{ story.headline|upper }}`).[1][3]

## Template Inheritance

Templates support inheritance via `{% extends "base.html" %}` and `{% block %}` tags, allowing child templates to override
sections of a parent for reusable layouts like headers or footers. This promotes code reuse across pages without duplicating
HTML boilerplate.[3][4][1]

## Usage Basics

Render templates in views using `render(request, 'template.html', context)`, where context is a dictionary of data; undefined
variables default to empty strings. Store templates in `templates/` directories configured in Django settings for app or
project-level organization.[2][4][1]

[1](https://docs.djangoproject.com/en/5.2/ref/templates/language/)
[2](https://www.pluralsight.com/resources/blog/guides/introduction-to-django-templates)
[3](https://realpython.com/django-templates-tags-filters/) [4](https://docs.djangoproject.com/en/5.2/topics/templates/)
[5](https://blog.jetbrains.com/pycharm/2025/02/the-ultimate-guide-to-django-templates/)
[6](https://www.geeksforgeeks.org/python/django-templates/) [7](https://www.w3schools.com/django/django_templates.php)
[8](https://www.youtube.com/watch?v=4uNeO5Hw9FE) [9](https://learndjango.com/tutorials/template-structure)
[10](https://www.youtube.com/watch?v=ZNrlc6TPcrU)
