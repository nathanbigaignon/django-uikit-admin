=====
UIKIT_ADMIN
=====

Uikit_admin is a modern grid based skin for Django built-in administration interface.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "uikit_admin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'uikit_admin',
    ]

2. Run `python manage.py migrate` to create the polls models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).