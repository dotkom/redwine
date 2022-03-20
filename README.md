# Redwine

RedWine is a simple Django app to conduct Web-based wine punishments. For each
user in their own comitee(s), users can add, delete and manage punishments.

## Quick start

1. Add "redwine" to your INSTALLED_APPS setting like this::

```python
INSTALLED_APPS = (
    ...
    'redwine',
)
```

2. Include the redWine URLconf in your project urls.py like this::

```python
re_path(r'^redwine/', include('redwine.urls')),
```

3. Run `python manage.py migrate` to create the redWine models.

4. Visit http://127.0.0.1:8000/redwine/ to do stuff.
