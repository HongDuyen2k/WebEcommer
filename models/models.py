from tokenize import Name
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


#################################
#####      DEFAULT   ############
#################################

STATUS = (
    ('True', 'True'),
    ('False', 'False')
)

STATUS_CART = (
    ('Done', 'Done'),
    ('Draft', 'Draft')
)

CODE_CATEGORY = (
    ('Clothes', 'Clothes'),
    ('Laptop', 'Laptop'),
    ('Phone', 'Phone')
)

STATUS_ORDER = (
    ('Draft', 'Draft'),
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Preparing', 'Preparing'),
    ('Shipping', 'Shipping'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled')
)

#################################
#####      USER   ###############
#################################

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, null=True, max_length=20)
    gender = models.CharField(blank=True, null=True, max_length=20)
    dateOfBirth = models.DateTimeField(auto_now=False, null=True, auto_now_add=False)
    image = models.ImageField(blank=True, null=True, upload_to='user_img')
    
    def __str__(self):
        return self.user.username
        
    def  image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" heights="50" width="50" />'.format(self.image.url))
        else:
            return ""
    
    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    noHome = models.IntegerField(null=True)
    street = models.CharField(blank=True, max_length=200)
    district = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=200)

    def full_address(self):
        return str(self.noHome) + ' ' + self.street + ' ' + self.district + ' ' + self.city

class CustomerMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(null=True)
    card = models.CharField(blank=True, max_length=200)

#################################
#####      Category   ###########
#################################

class Category(models.Model):
    name = models.CharField(blank=True, max_length=200)
    code = models.CharField(max_length=20, choices=CODE_CATEGORY)
    details = models.CharField(blank=True, max_length=200)
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.name

#################################
#####      Product   ############
#################################
class Clothes(models.Model):
    name = models.CharField(blank=True, max_length=200)
    brand = models.CharField(blank=True, max_length=200)
    material = models.CharField(blank=True, max_length=200)
    design = models.CharField(blank=True, max_length=200)
    type = models.CharField(blank=True, max_length=200)
    madeIn = models.CharField(blank=True, max_length=200)
    manufactureDate = models.DateField()

    def __str__(self):
        return self.name

class ImageClothes(models.Model):
    image = models.ImageField(blank=True, upload_to='clothes_img')
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="50" />'.format(self.image.url))

    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

class ColorClothes(models.Model):
    name = models.CharField(blank=True, max_length=200)
    code = models.CharField(blank=True, max_length=200)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)

    def __str__(self):
            return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""

class SizeClothes(models.Model):
    name = models.CharField(blank=True, max_length=200)
    size = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ClothesItem(models.Model):
    name = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='clothes_item_img')
    barcode = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    price = models.FloatField()
    discount = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="50" />'.format(self.image.url))

    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def new_price(self):
        return self.price * ((100 - self.discount) % 100);

#################################
#####      Phone   ##############
#################################
class Phone(models.Model):
    name = models.CharField(blank=True, max_length=200)
    version = models.CharField(blank=True, max_length=200)
    madeIn = models.CharField(blank=True, max_length=200)
    yearOfManufacture = models.IntegerField()
    type = models.CharField(blank=True, max_length=200)
    ram = models.CharField(blank=True, max_length=200)
    memory = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.name

class ImagePhone(models.Model):
    image = models.ImageField(blank=True, upload_to='clothes_img')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="50" />'.format(self.image.url))

    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

class ColorPhone(models.Model):
    name = models.CharField(blank=True, max_length=200)
    code = models.CharField(blank=True, max_length=200)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
            return self.name


class PhoneItem(models.Model):
    name = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='clothes_item_img')
    barcode = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    price = models.FloatField()
    discount = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="50" />'.format(self.image.url))

    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def new_price(self):
        return self.price * ((100 - self.discount) % 100);

#################################
#####      Cart   ###############
#################################

class Cart(models.Model):
    name = models.CharField(blank=True, max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    information = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CART)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothesItem = models.ForeignKey(ClothesItem, null=True, on_delete=models.CASCADE)
    phoneItem = models.ForeignKey(PhoneItem, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#################################
#####  Voucher - Shipment   #####
#################################

class Voucher(models.Model):
    name = models.CharField(blank=True, max_length=200)
    code = models.CharField(blank=True, max_length=200)
    discountPercent = models.FloatField()

    def __str__(self):
        return self.name

class Shipment(models.Model):
    name = models.CharField(blank=True, max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name

#################################
#####      Comment   ############
#################################

class Feedback(models.Model):
    subject = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=500, blank=True)
    rate = models.IntegerField(default=1)
    status = models.CharField(max_length=40, choices=STATUS)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothesItem = models.ForeignKey(ClothesItem, null=True, on_delete=models.CASCADE)
    phoneItem = models.ForeignKey(PhoneItem, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

#################################
#####      Order     ############
#################################

class Order(models.Model):
    totalPriceBefore = models.FloatField()
    totalPriceAfter = models.IntegerField()
    information = models.TextField()
    note = models.TextField()
    status = models.CharField(max_length=40, choices=STATUS_ORDER)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, null=True, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class OrderCart(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)

#################################
#####      Payment    ###########
#################################

class Payment(models.Model):
    price = models.FloatField()
    codeBill = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.codeBill