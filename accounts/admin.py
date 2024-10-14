from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'username', 'date_joined', 'last_login', 'is_active']
    readonly_fields = ['last_login', 'date_joined']
    list_display_links = ['email', 'username']

    list_filter = ()
    filter_horizontal = ()
    # for setting password as a non editable field
    fieldsets = ()


admin.site.register(Account, AccountAdmin)