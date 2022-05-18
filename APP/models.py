from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
    )
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=274)
    email = models.EmailField()
    occputation = models.CharField(max_length=30)
    salary = models.IntegerField()
    gender = models.CharField(max_length=255, null=True, choices=GENDER)
    
    
    
    def __str__(self):
        return self.name
    
    
    
    def get_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'occputation': self.occputation,
            'salary': self.salary,
            'gender': self.gender,
        }
    