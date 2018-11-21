from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class T_user(models.Model):
    SEX_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )
    account = models.CharField(max_length=250)
    idt = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=20)
    self_ID = models.CharField(max_length=18)
    address = models.CharField(max_length=200)
    author = models.ForeignKey(User,
                                on_delete = models.CASCADE,    
                                related_name='tree_posts')
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sex = models.CharField(max_length=10,choices=SEX_CHOICES)
    
    class Meta:
           ordering = ('-publish',)
		
    def __str__(self):
        return self.account
    
class T_card(models.Model): 
        account = models.CharField(max_length=250)
        card = models.CharField(max_length = 20)
        card_pass = models.CharField(max_length = 6)
        def __str__(self):
            return self.card

class T_goods(models.Model):
    SIZE_CHOICES = (
        ('s', 's'),
        ('m', 'm'),
        ('l','l'),
    )
    account = models.CharField(max_length=250)
    good_name = models.CharField(max_length=250)
    good_id = models.CharField(max_length=250)
    price = models.FloatField
    size = models.CharField(max_length=10,choices=SIZE_CHOICES)
    color = models.CharField(max_length=250)
    number = models.IntegerField
    def _str_(self):
        return self. good_name 