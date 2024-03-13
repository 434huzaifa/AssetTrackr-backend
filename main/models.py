from django.db import models
from django.db.models import CharField,EmailField,DecimalField,TextField,UUIDField
import uuid
# Create your models here.
class Company(models.Model):
    id=UUIDField(primary_key=True,default=uuid.uuid4(),editable=False)
    title=CharField(max_length=150,null=True,blank=True)
    email=EmailField(null=True,blank=True,unique=True)
    password=CharField(max_length=10,null=True,blank=True)
    
    def __str__(self):
        return f'{self.title}'