from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True)
    description = models.TextField(blank=True, db_index=True, null=True)
    price = models.FloatField(db_index=True, null=True)
    tags = models.ManyToManyField(Tag, db_index=True, null=True)

    def __str__(self):
        return self.name
