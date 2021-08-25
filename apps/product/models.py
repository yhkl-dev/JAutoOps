from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ProductModel(models.Model):
    product_name = models.CharField('product_name', max_length=50, null=False, unique=True, help_text='product name')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='create user', null=False,
                                    related_name='created_user', help_text='create user')
    create_time = models.DateTimeField('create_time', auto_now_add=True, help_text='create time')
    update_time = models.DateTimeField('update_time', auto_now=True, help_text='update time')

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['id']
        db_table = 't_product'
