from django.db import models

from gm2m import GM2MField


class TModel(models.Model):
    name = models.CharField(max_length=200)

    test = GM2MField()

    for_inline = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='inline_test_models'
    )

    def __str__(self):
        return self.name
