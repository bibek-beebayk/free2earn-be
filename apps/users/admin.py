from django.contrib import admin

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Refugee)
class RefugeeAdmin(admin.ModelAdmin):
    pass


@admin.register(OrganizationUser)
class OrganizationUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass


@admin.register(PublicUser)
class PublicUserAdmin(admin.ModelAdmin):
    pass