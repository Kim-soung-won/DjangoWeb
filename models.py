# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    brand_name = models.CharField(unique=True, max_length=100)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'


class Cart(models.Model):
    created_who = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='created_who', primary_key=True)  # The composite primary key (created_who, product_id, size) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    size = models.CharField(max_length=10)
    count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'
        unique_together = (('created_who', 'product', 'size'),)


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    created_who = models.BigIntegerField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class CommentImg(models.Model):
    img_id = models.BigAutoField(primary_key=True)
    comment = models.ForeignKey(Comment, models.DO_NOTHING)
    img_url = models.CharField(max_length=4000)
    img_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'comment_img'


class Coupon(models.Model):
    coupon_id = models.BigAutoField(primary_key=True)
    used = models.IntegerField(blank=True, null=True)
    coupon_name = models.CharField(max_length=255)
    discount_size = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    used_at = models.DateTimeField(blank=True, null=True)
    discount_price = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon'


class CsAnswer(models.Model):
    cs = models.OneToOneField('CustomerService', models.DO_NOTHING, primary_key=True)
    created_who = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs_answer'


class CustomerService(models.Model):
    cs_id = models.BigAutoField(primary_key=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_service'


class Delivery(models.Model):
    delivery_id = models.BigAutoField(primary_key=True)
    payment = models.ForeignKey('Payment', models.DO_NOTHING)
    tg_pnum = models.CharField(max_length=20)
    tg_address = models.CharField(max_length=100)
    state = models.CharField(max_length=8, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Love(models.Model):
    product = models.OneToOneField('Product', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, created_who, created_at) found, that is not supported. The first column is selected.
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'love'
        unique_together = (('product', 'created_who', 'created_at'),)


class Payment(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    total_price = models.IntegerField()
    size = models.CharField(max_length=10, blank=True, null=True)
    count = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    pd_name = models.CharField(max_length=100)
    pd_price = models.IntegerField()
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    pd_category = models.TextField(blank=True, null=True)
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    count_love = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductDetail(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=10)
    pd_before_count = models.IntegerField(blank=True, null=True)
    pd_sell_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_detail'
        unique_together = (('product', 'size'),)


class ProductLog(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, created_at, created_who) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=10)
    count = models.IntegerField()
    created_who = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='created_who')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_log'
        unique_together = (('product', 'created_at', 'created_who'),)


class Recommend(models.Model):
    created_who = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='created_who', primary_key=True)
    product_list = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'recommend'


class Testcomment(models.Model):
    image_name = models.CharField(max_length=50, blank=True, null=True)
    image_content = models.CharField(max_length=4000, blank=True, null=True)
    image_filename = models.CharField(max_length=100)
    image_originalname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'testcomment'


class UserAccount(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_email = models.CharField(unique=True, max_length=100)
    user_password = models.CharField(max_length=100)
    user_role = models.CharField(max_length=7, blank=True, null=True)
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
    name = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class UserLog(models.Model):
    userlog_id = models.BigAutoField(primary_key=True)
    created_who = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    doit = models.CharField(max_length=7, blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_log'
