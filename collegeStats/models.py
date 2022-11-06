from django.db import models


class College(models.Model):
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name
