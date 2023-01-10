from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class Plan(models.Model):
    DURATION = (
        ('1 Month', '1 Month'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('Other', 'Other')
    )
    plan_name = models.CharField(max_length=250, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True, help_text="Enter details")
    Duration = models.TextField(choices=DURATION, default='')
    cost = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return str(self.plan_name)


class Userprofile(models.Model):
    user = models.CharField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, blank=True, null=True)
    address = models.TextField()
    #profile_image = models.ImageField(blank=True, null=True, default='images/profile.png', upload_to='profiles')
    #phone_number = PhoneNumberField(null=False, blank=False, unique=True, default='+972')
    #current_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default='')


class MyUserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """Create and save a User with the given username and password."""
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        """Create and save a regular User with the given username and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given username and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=250)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = raw_password

    def check_password(self, raw_password):
        return self.password == raw_password

    def __str__(self):
        return self.email