from django.db import models

# Create your models here.
class Furniture(models.Model):
    furn_name = models.CharField(max_length=130)
    furn_image = models.ImageField(upload_to='images/', null=True, blank=True)
    furn_price = models.IntegerField(null=True)
    furn_description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.furn_name
    

class Gadget(models.Model):
    gadget_name = models.CharField(max_length=30)
    gadget_image = models.ImageField(upload_to='images/', null=True, blank=True)
    gadget_price = models.IntegerField()
    gadget_description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.gadget_name

class Fashion(models.Model):
    nname = models.CharField(max_length=20)
    def __str__(self):
        return self.nname

class Shirt(models.Model):
    shirt_name = models.CharField(max_length=20)
    shirt_category = models.ForeignKey(Fashion, on_delete=models.CASCADE)
    shirt_image = models.ImageField(upload_to='images/', null=True, blank=True)
    shirt_price = models.IntegerField()
    shirt_description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.shirt_name
    
class Trouser(models.Model):
    trouser_name = models.CharField(max_length=20)
    trouser_category = models.ForeignKey(Fashion, on_delete=models.CASCADE)
    trouser_image = models.ImageField(upload_to='images/', null=True, blank=True)
    trouser_price = models.IntegerField()
    trouser_description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.trouser_name

class Sneaker(models.Model):
    sneaker_name = models.CharField(max_length=20)
    sneaker_category = models.ForeignKey(Fashion, on_delete=models.CASCADE)
    sneaker_image = models.ImageField(upload_to='images/', null=True, blank=True)
    sneaker_price = models.IntegerField()
    sneaker_description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.sneaker_name

class Attire(models.Model):
    attire_name = models.CharField(max_length=20)
    attire_category = models.ForeignKey(Fashion, on_delete=models.CASCADE)
    attire_image = models.ImageField(upload_to='images/', null=True, blank=True)
    attire_price = models.IntegerField()
    attire_description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.attire_name


class Dog(models.Model):
    pet_name = models.CharField(max_length=20)
    pet_image = models.ImageField(upload_to='images/', null=True, blank=True)
    pet_price = models.IntegerField()
    pet_description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.pet_name

class PhoneCategory(models.Model):
    phone_category = models.CharField(max_length=8)
    def __str__(self):
        return self.phone_category

class Phone(models.Model):
    phone_name = models.CharField(max_length=20)
    phone_model = models.ForeignKey(PhoneCategory, on_delete=models.CASCADE, null=True, blank=True)
    phone_image = models.ImageField(upload_to='images/', null=True, blank=True)
    phone_price = models.IntegerField()
    phone_description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.phone_name
    
