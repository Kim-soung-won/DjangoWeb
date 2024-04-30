# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    brand_name = models.CharField(unique=True, max_length=100)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'


class Cart(models.Model):
    count = models.IntegerField(blank=True, null=True)
    created_who = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='created_who', primary_key=True)  # The composite primary key (created_who, product_id, size) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    size = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cart'
        unique_together = (('created_who', 'product', 'size'),)


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    content = models.CharField(max_length=255)
    created_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class CommentImg(models.Model):
    comment = models.ForeignKey(Comment, models.DO_NOTHING, blank=True, null=True)
    img_id = models.BigAutoField(primary_key=True)
    img_name = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_img'


class Coupon(models.Model):
    discount_price = models.IntegerField(blank=True, null=True)
    discount_size = models.IntegerField(blank=True, null=True)
    used = models.TextField(blank=True, null=True)  # This field type is a guess.
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    coupon_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    used_at = models.DateTimeField(blank=True, null=True)
    coupon_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon'


class CsAnswer(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    cs = models.OneToOneField('CustomerService', models.DO_NOTHING, primary_key=True)
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs_answer'


class CustomerService(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    cs_id = models.BigAutoField(primary_key=True)
    payment_id = models.BigIntegerField()
    content = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_service'


class Delivery(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    delivery_id = models.BigAutoField(primary_key=True)
    payment = models.OneToOneField('Payment', models.DO_NOTHING, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tg_address = models.CharField(max_length=255)
    tg_pnum = models.CharField(max_length=255)
    state = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class Love(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    created_who = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='created_who', primary_key=True)  # The composite primary key (created_who, product_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'love'
        unique_together = (('created_who', 'product'),)


class Payment(models.Model):
    count = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    payment_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    delivery_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    count_love = models.IntegerField(blank=True, null=True)
    product_price = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    product_id = models.BigAutoField(primary_key=True)
    product_category = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255)
    product_img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductDetail(models.Model):
    pd_before_count = models.IntegerField(blank=True, null=True)
    pd_sell_count = models.IntegerField(blank=True, null=True)
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_detail'
        unique_together = (('product', 'size'),)


class ProductImg(models.Model):
    img_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    img_url = models.CharField(max_length=255)
    img_name = models.CharField(max_length=255)
    created_who = models.BigIntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_img'


class ProductLog(models.Model):
    count = models.IntegerField()
    created_at = models.DateTimeField(primary_key=True)  # The composite primary key (created_at, created_who, product_id) found, that is not supported. The first column is selected.
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who')
    product = models.ForeignKey(Product, models.DO_NOTHING)
    size = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_log'
        unique_together = (('created_at', 'created_who', 'product'),)


class Recommend(models.Model):
    created_who = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='created_who', primary_key=True)
    product_list = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'recommend'


class UserAccount(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_email = models.CharField(unique=True, max_length=100)
    user_password = models.CharField(max_length=100)
    user_role = models.CharField(max_length=20, blank=True, null=True)
    user_pnum = models.CharField(max_length=20)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account'


class UserImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_name = models.CharField(max_length=255, blank=True, null=True)
    image_content = models.CharField(max_length=255, blank=True, null=True)
    image1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_image'


class UserInfo(models.Model):
    user = models.OneToOneField(UserAccount, models.DO_NOTHING, primary_key=True)
    name = models.CharField(unique=True, max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class UserLog(models.Model):
    userlog_id = models.BigAutoField(primary_key=True)
    created_who = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    doit = models.CharField(max_length=7, blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_log'
