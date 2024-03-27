from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User, AddressModel


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['first_name', 'last_name', 'email', 'company_name']
    list_filter = ['is_active']
    readonly_fields = ['last_login']

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'trn_number', 'company_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'trn_number', 'company_name', 'password')}),
    )

    search_fields = ['first_name', 'last_name', 'email', 'phone_number', 'trn_number', 'company_name']
    ordering = ['first_name', 'last_name']

    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(AddressModel)
admin.site.unregister(Group)
