from django.contrib import admin

from users.models import User, Payments, Subscribe

admin.site.register(User)

admin.site.register(Payments)

admin.site.register(Subscribe)
