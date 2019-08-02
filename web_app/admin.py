from django.contrib import admin

# Register your models here.
admin.site.site_header = '后台管理'
admin.site.site_title = '后台管理'

from web_app.models import *

admin.site.register(News, NewsAdmin)  # NewsAdmin单独注册报错
admin.site.register(NewsClass)