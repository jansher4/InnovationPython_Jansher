from django.db import models

# Create your models here.
class JuniorStudents(models.Model):
    name = models.CharField(max_length=20)
    id1 = models.IntegerField()
    contact = models.IntegerField()
    address = models.CharField(max_length= 50)

    def __str__(self):
        return self.name
class SophomoreStudents(models.Model):
    name = models.CharField(max_length=20)
    id1 = models.IntegerField()
    contact = models.IntegerField()
    address = models.CharField(max_length= 50)

    def __str__(self):
        return self.name
class SeniorStudents(models.Model):
    name = models.CharField(max_length=20)
    id1 = models.IntegerField()
    contact = models.IntegerField()
    address = models.CharField(max_length= 50)

    def __str__(self):
        return self.name