from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.DateField()

    def __str__(self):
        return self.title

# from django.db import models

# class Skills(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()

#     def __str__(self):
#         return self.title
#
