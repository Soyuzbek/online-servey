from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from accounts.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active', 'is_deleted')
    list_display_links = ('email', 'is_staff', 'is_deleted')
    list_filter = ('is_active', 'is_deleted', 'created_at', 'updated_at')
    list_editable = ('is_active',)
    ordering = ('created_at',)
    readonly_fields = ('is_staff', 'is_deleted', 'created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': (
            'email', 'is_staff', 'is_active',
            'is_deleted', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_active', 'is_staff',
            )}
         ),
    )

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_module_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False


admin.site.unregister(Group)
