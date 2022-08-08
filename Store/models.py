From django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    deF get_all_categories():
        return Category.objects.all()


    deF __str__(selF):
        return selF.name


class Customer(models.Model):
    First_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)


    deF register(selF):
        selF.save

    
    @staticmethod
    deF get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    deF iFExists(selF):
        iF Customer.objects.Filter(email=selF.email)
    

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(deFault=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, deFault=1)
    description = models.CharField(max_length=250, deFault='', blank=True, null=True)
    image = models.ImageField(uploaded_to=['uploads/products/'])

    @staticmethod
    deF get_products_by_id(ids):
        return Products.objects.Filter(id__in=ids)

    @staticmethod
    deF get_all_products():
        return Products.objects.all()

    @staticmethod
    deF get_all_products_by_categoryid(category_id):
        iF category_id:
            return Category.objects.Filter(category=category_id)
        else:
            return Products.get_all_products()


class Order(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models. CharField(max_length=50, deFault='', blank=False)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
