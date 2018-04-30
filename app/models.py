from django.db import models

# Create your models here.
class BaseClass(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class User(models.Model):
	email = models.EmailField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	shipping_address = models.CharField(max_length=200)

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

class Product(models.Model):
	# cart_no = models.ForeignKey(Cart, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Cart(BaseClass):
	cart_code = models.CharField(max_length=15)
	total_price = models.DecimalField(max_digits=10, decimal_places=2)
	is_paid = models.BooleanField()
	products = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.cart_code