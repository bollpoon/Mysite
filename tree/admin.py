from django.contrib import admin
from .models import T_user,T_card,T_goods


class T_userAdmin(admin.ModelAdmin):
    list_display = ('account', 'id', 'password', 'address')
admin.site.register(T_user, T_userAdmin)

class T_cardAdmin(admin.ModelAdmin):
    list_display = ('account', 'card', 'card_pass')
admin.site.register(T_card, T_cardAdmin)

class T_goodsAdmin(admin.ModelAdmin):
    list_display = ('account', 'good_name', 'price', 'number')
admin.site.register(T_goods, T_goodsAdmin)
