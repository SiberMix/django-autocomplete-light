from django.db import models

from genericm2m.models import RelatedObjectsDescriptor


class TModel(models.Model):
    name = models.CharField(max_length=200)

    test = RelatedObjectsDescriptor()

    for_inline = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='inline_test_models'
    )

    def __str__(self):
        return self.name
