from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)

    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    model_name = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.BooleanField()
    image = models.FileField()
    # attributes = models.ForeignKey(Attribute, on_delete=CASCADE)
    characteristics = {}
    
    
    def __str__(self):
        return self.name + ' ' + self.model_name


class AttributeGroup(models.Model):
    name = models.CharField(max_length=256)

    
    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=256)
    attribute_group = models.ForeignKey(AttributeGroup, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=256)
    

    def __str__(self):
        return self.name


class Filter(models.Model):
    name = models.CharField(max_length=256)
    

    def __str__(self):
        return self.name




