django-taggit TaggableManager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Model example
=============

Consider such a model, using `django-taggit
<https://github.com/alex/django-taggit>`_ to handle tags for a model:

.. code-block:: python

    from django.db import models

    from taggit.managers import TaggableManager


    class TestModel(models.Model):
        name = models.CharField(max_length=200)

        tags = TaggableManager()

        def __str__(self):
            return self.name

View example
============

The :ref:`QuerySet view<queryset-view>` works here too: we're relying on
Select2 and a QuerySet of Tag objects:

.. code-block:: python

    from dal import autocomplete

    from taggit.models import Tag


    class TagAutocomplete(autocomplete.Select2QuerySetView):
        def get_queryset(self):
            # Don't forget to filter out results depending on the visitor !
            if not self.request.user.is_authenticated():
                return Tag.objects.none()

            qs = Tag.objects.all()

            if self.q:
                qs = qs.filter(name__istartswith=self.q)

            return qs

        def get_create_option(self, context, q):
            return []

Don't forget to :ref:`register-view`.

.. note:: For more complex filtering, refer to official documentation for
          the :django:label:`queryset-api`.

Form example
============

As usual, we need a backend-aware widget that will make only selected choices
to render initially, to avoid butchering the database.

As we're using a QuerySet of Tag and Select2 in its "tag" appearance, we'll use
:py:class:`~dal_select2_taggit.widgets.TaggitSelect2`. It is compatible with
the default form field created by the model field: TaggeableManager - which
actually inherits ``django.db.models.fields.Field`` and
``django.db.models.fields.related.RelatedField`` and **not** from
``django.db.models.Manager``.

Example:

.. code-block:: python

    class TestForm(autocomplete.FutureModelForm):
        class Meta:
            model = TestModel
            fields = ('name',)
            widgets = {
                'tags': autocomplete.TaggitSelect2(
                    'your-taggit-autocomplete-url'
                )
            }
