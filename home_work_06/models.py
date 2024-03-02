from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=128)  # В реальном приложении пароль должен быть захеширован

class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    description = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)

class Order(Model):
    id = fields.IntField(pk=True)
    user_id = fields.ForeignKeyField('models.User', related_name='orders')
    product_id = fields.ForeignKeyField('models.Product', related_name='orders')
    order_date = fields.DatetimeField(auto_now_add=True)
    status = fields.CharField(max_length=50)
