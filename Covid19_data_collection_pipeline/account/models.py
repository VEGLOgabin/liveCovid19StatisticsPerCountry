from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, password,email,sexe,country,date_inscription,telephone,photo,description, **kwargs):
        """
        Creates and saves a User with the given phone and password.
        """
        email=self.normalize_email(email)
        if not email:
            raise ValueError('Users must have email')
        
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email=email,
            sexe=sexe,
            country = country,
            date_inscription=date_inscription,
            telephone=telephone,
            photo=photo,
            description=description
        )

        user.is_active = True
        user.admin = False
        user.staff = False

        user.set_password(password)
        user.save()

        return user
    

    def create_staffuser(self, first_name, last_name,password,email,sexe,country,date_inscription,telephone,photo,description):

        email=self.normalize_email(email)
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            email=email,
            sexe=sexe,
            country = country,
            date_inscription=date_inscription,
            telephone=telephone,
            photo=photo,
            password=password,
            description=description
        )

        user.staff = True
        user.is_active = True


        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, email,password,sexe,country,date_inscription,telephone,photo,description):
        email=self.normalize_email(email)
        user = self.create_user(
            
            first_name = first_name,
            last_name = last_name,
            email=email,
            sexe=sexe,
            date_inscription=date_inscription,
            telephone=telephone,
            photo=photo,
            password=password,
            description=description,
            country = country
            
            
        )
        
        

        user.admin = True
        user.staff = True
        user.is_active = True
        
        user.save()
        return user




class User(AbstractBaseUser,PermissionsMixin):
    # ROLES = (('student', 'Student'), ('FORMATEUR EXTAINE', 'FORMATEUR EXTAINE'),('PERSONNEL','PERSONNEL'),('STAGIAIRE','STAGIAIRE'))
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    sexe=models.CharField(blank=False,max_length=50)
    date_inscription=models.DateTimeField(auto_now=True)
    telephone=models.IntegerField()
    description = models.CharField(max_length=300,null=True,blank=True)
    photo=models.ImageField(upload_to='PROFIL_IMG')
    country = models.CharField(max_length=255,null=True,blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','sexe','date_inscription','telephone','country']

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
       return self.first_name

    
