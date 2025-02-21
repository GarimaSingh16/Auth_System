from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Remove 'groups' and 'user_permissions' fields as they're not in CustomUser
    filter_horizontal = ()
    list_filter = ('is_active',)  # Use the fields that are available in CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')  # Adjust as needed
    search_fields = ('email', 'first_name', 'last_name')  # You can search by these fields
    ordering = ('email',)

    # Define fieldsets (remove references to non-existent fields like groups)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'organization')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
