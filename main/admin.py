from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import account
# Register your models here


class UserAdminConfig(UserAdmin):
    model = account
    ordering = ('-date_joined', )
    search_fields = ('name', 'email', 'username')
    list_display = ('name', 'email', 'username', 'is_active', 'is_superuser')
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_admin')

    fieldsets = (
        (None, {
            'fields': ('name', 'dob', 'email', 'username', 'mobile')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff', 'is_active', 'is_admin')
        }),
    )

    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('name', 'dob', 'email', 'username', 'password1', 'mobile',
                   'password2', 'is_staff', 'is_active'),
    }), )


admin.site.register(account, UserAdminConfig)
