from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Product Name'))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Product Price'))
    stock = models.IntegerField(verbose_name=_('Product Stock'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('Product Category'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Category Name'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
