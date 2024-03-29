from django.db import models

from tagging.fields import TagField


class TModel(models.Model):
    name = models.CharField(max_length=200)

    test = TagField()

    for_inline = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='inline_test_models'
    )

    def __str__(self):
        return self.name
