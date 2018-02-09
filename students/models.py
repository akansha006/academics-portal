from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=40)
    roll = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Marks(models.Model):
    name = models.ForeignKey(
        'Students',
        on_delete=models.CASCADE,
    )
    subject = models.CharField(max_length=30)
    mark = models.FloatField()

    def __str__(self):
        return self.subject
