from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


#Creating user manager for handling user creation
class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_("The email must be provided"))
        email = self.normalize_email(email)
        user = self.model(email = email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        
        if kwargs.get('is_staff') != True:
            raise ValueError(_('is_staff must be True'))
        if kwargs.get('is_superuser') != True:
            raise ValueError(_('is_superuser must be True'))
        
        return self.create_user(email, password, **kwargs)
    
    

#Creating a user model to store user information in a RDBMS database
class UserModel(AbstractUser):
    username = None
    email = models.EmailField(unique=True, db_index=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return self.email