from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length = 50)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name   


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Indigo = 'Indigo'
    Violet = 'Violet'
    White = 'White'
    Black = 'Black'

    Shoe_color_choices = [
    (Red, 'Red'), (Orange, 'Orange'), 
    (Yellow, 'Yellow'),
    (Green, 'Green'),
    (Blue, 'Blue'),
    (Indigo, 'Indigo'),
    (Violet, 'Violet'),
    (White, 'White'),
    (Black, 'Black'),
    ]

    color_name = models.CharField(max_length=10, choices=Shoe_color_choices, default=Orange)
    
    def __str__(self):
        return self.color_name



class Shoe(models.Model):
    size = models.CharField(max_length =100)
    brand_name = models.CharField(max_length =100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length =100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length =100)

