from django.contrib import admin
from .models import Activity, Player

# Register your models here.
admin.site.register(Activity)
admin.site.register(Player)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# admin.site.unregister(User)

# class opetestAdmin(admin.ModelAdmin):
#     pass

# class UserProfileInline(admin.StackedInline):
#     filter_horizontal = ('ope',)

# class CustomUserAdmin(UserAdmin):
#     #filter_horizontal = ('user_permissions', 'groups', 'ope')
#     save_on_top = True
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login')
#     inlines = [UserProfileInline]

# admin.site.register(User, CustomUserAdmin)
# # admin.site.register(opetest, opetestAdmin)