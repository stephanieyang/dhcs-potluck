from django.contrib import admin

# Register your models here.
from .models import UserInfo, UserComment, SaleItem
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
#from Connect_FMS.models import UserProfile

"""
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = True

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
"""


admin.site.register(UserInfo)
admin.site.register(UserComment)
admin.site.register(SaleItem)
#admin.site.register(Post)
#admin.site.register(PostComment)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

