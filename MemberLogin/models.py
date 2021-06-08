from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

USER_TYPES = (
    ('Mentor','Mentor'),
    ('HR','HR'),
    ('MARKETING','Marketing')
)

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, user_type, password = None):
        if not email:
            raise ValueError("Users must have a valid email address.")
        if not username:
            raise ValueError("Users must have a valid username.")
        if not user_type:
            raise ValueError("Users must have a valid user type.")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            user_type = user_type,
        )
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_superuser(self, email, username, user_type, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            user_type= user_type,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_admin = True

        user.save(using= self._db)
        return user


class NewUser(AbstractBaseUser):
    email                       = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username                    = models.CharField(max_length=30,unique=True)
    date_joined                 = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login                  = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin                    = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    is_staff                    = models.BooleanField(default=False)
    is_superuser                = models.BooleanField(default=False)
    user_type                   = models.CharField(choices=USER_TYPES, max_length=128)
    phone_number                = PhoneNumberField(blank=True,unique=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','user_type']

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm ,obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

