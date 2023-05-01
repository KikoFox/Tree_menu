from django.contrib import admin
from menu.models import Menu, MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'is_visible', 'order')
    list_editable = ('is_visible', 'order')
    list_filter = ('parent',)


class MenuAdmin(admin.ModelAdmin):
    pass


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
