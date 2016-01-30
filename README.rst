=====
Django Uikit Admin
=====

Django Uikit Admin is a modern grid based skin for Django built-in administration interface.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install Django Uikit Admin using pip::

    pip install django-uikit-admin

2. Add "uikit_admin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        'uikit_admin',
        ...
    ]

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).
