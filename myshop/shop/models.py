from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models

# Create your models here.
from django.db.models import Manager


class Product(models.Model):
    UNITS = (
        (1, 'шт.'),
        (2, 'кг.'),
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    name = models.CharField(verbose_name='название', max_length=128)
    date = models.DateField(verbose_name='дату поступления')
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=0, default=0)
    unit = models.IntegerField(verbose_name='еденица измерения', choices=UNITS)
    provider = models.CharField(verbose_name='имя поставщика', max_length=256, blank=True)
    objects = Manager()
    site = models.ManyToManyField(Site, null=True)
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    products = models.ManyToManyField(Product)
    objects = Manager()
    site = models.ForeignKey(Site,on_delete=models.CASCADE, null=True)
    on_site = CurrentSiteManager('site')


    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

class DescriptionProduct(models.Model):
    text = models.CharField(max_length=64)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # deleted = models.BooleanField(default=False, null=False)


    def __str__(self):
        return self.text

