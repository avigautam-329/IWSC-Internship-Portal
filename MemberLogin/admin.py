from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from MemberLogin.models import NewUser

# Register your models here.

class UserAdmin(UserAdmin):
    list_display = ('email', 'username','user_type','phone_number','date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    radio_fields = {'user_type' : admin.VERTICAL}

    #Random fields.
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(NewUser, UserAdmin)