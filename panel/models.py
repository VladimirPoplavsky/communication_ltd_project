from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Plan(models.Model):
    DURATION = (
        ('1 Month', '1 Month'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('Other', 'Other')
    )
    plan_name = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True, help_text="Enter details")
    Duration = models.TextField(choices=DURATION, default='')
    cost = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return str(self.plan_name)


class Userprofile(models.Model):
    user = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.TextField()
    profile_image = models.ImageField(blank=True, null=True, default='images/profile.png', upload_to='profiles')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, default='+972')
    current_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default='')
