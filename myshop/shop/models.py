from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)


    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


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
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name