from django.contrib import admin
from menu.models import MenuCategories


class MenuCategoriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(MenuCategories, MenuCategoriesAdmin)
