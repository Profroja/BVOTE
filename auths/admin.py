from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Show role in the list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')

    # Include the role field in the user edit form
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )

    # Include the role field in the add user form
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )
