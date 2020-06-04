from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from enum import Enum



class MyAccountManager(BaseUserManager):
    def create_user(self, email, full_name, phone, password=None):
        if not email:
            return ValueError("User must have an email address")
        if not full_name:
            return ValueError("User must enter their name")
        if not phone:
            return ValueError("User must enter the phone number")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            phone=phone,
            password=password,
        )
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=500)
    email = models.EmailField(max_length=60, unique=True)
    phone = models.IntegerField()
    hash = models.TextField(max_length=256)
    salt = models.TextField(max_length=32)
    onboarded_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['full_name', 'phone']

    objects = MyAccountManager()


# class Locations(models.Model):
#     id = models.IntegerField(primary_key=True)
#     longitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     latitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    first_line = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
    pin_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=3)


class Partner(models.Model):
    id = models.IntegerField(primary_key=True)
    # name = models.CharField(max_length=500)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    email = models.EmailField
    onboarded_at = models.DateTimeField(auto_now=True)


class DayChoice(Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"




class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=256)
    store_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    # location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    google_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    store_type = models.CharField(max_length=500)
    gstin = models.CharField(max_length=20)
    onboarded_at = models.DateTimeField(auto_now=True)
    no_of_lockers = models.IntegerField()
    avg_length=models.IntegerField()
    avg_breadth=models.IntegerField()
    no_of_cctv = models.IntegerField()
    # ease_of_transprtation = models.BooleanField(default=False)

class StoreTimings(models.Model):
    id = models.IntegerField(primary_key=True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    open_day = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in DayChoice]
    )
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()



