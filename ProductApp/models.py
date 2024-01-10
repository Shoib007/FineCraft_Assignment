from django.db import models
from uuid import uuid4
from mongo_config import db


# Create your models here.
def filePath(instance, filename):
    return "/".join([str(instance.id), filename])

class ProductModel(models.Model):
    id = models.UUIDField( default=uuid4, primary_key=True, db_index=True, unique=True)
    image = models.ImageField(upload_to=filePath)
    
    def __str__(self) -> str:
        return str(self.id)
    
    

product_collection = db['Product']