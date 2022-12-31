from django.db import models

# Create a model for database. Here, we are creating a member's database model
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    # one way to show the detail in django admin
    # def __str__(self):
        #return f"{self.firstname} {self.lastname}"
    # the other way is done in the admin.py itself


