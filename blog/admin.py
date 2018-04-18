from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import  *

admin.site.register(Report)
admin.site.register(User)
admin.site.register(App)
admin.site.register(View)




