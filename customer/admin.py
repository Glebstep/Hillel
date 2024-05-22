# from django.contrib import admin
# from .models import MenuItem,Category,OrderModel

# admin.site.register(MenuItem)
# admin.site.register(Category)
# admin.site.register(OrderModel)


from django.contrib import admin
from .models import MenuItem, Category, OrderModel

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name', 'category__name')
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'price', 'name', 'email')
    search_fields = ('name', 'email', 'items__name')
    list_filter = ('items__name',)