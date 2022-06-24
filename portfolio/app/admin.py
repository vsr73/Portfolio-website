from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(user)
class Adminuser(admin.ModelAdmin):
    list_display =[field.name for field in user._meta.fields]

@admin.register(skills)
class Adminskills(admin.ModelAdmin):
 	list_display =[field.name for field in skills._meta.fields]

@admin.register(coding_languages)
class Admincoding_languages(admin.ModelAdmin):
 	list_display =[field.name for field in coding_languages._meta.fields]

@admin.register(services)
class Adminsupport(admin.ModelAdmin):
 	list_display =[field.name for field in services._meta.fields]

@admin.register(support)
class Adminsupport(admin.ModelAdmin):
 	list_display =[field.name for field in support._meta.fields]


@admin.register(projects)
class Adminprojects(admin.ModelAdmin):
 	list_display =[field.name for field in projects._meta.fields]

@admin.register(comment)
class Admincodingcomment(admin.ModelAdmin):
 	list_display =[field.name for field in comment._meta.fields]

@admin.register(reply)
class Adminreply(admin.ModelAdmin):
 	list_display =[field.name for field in reply._meta.fields]

@admin.register(blog)
class Adminblog(admin.ModelAdmin):
 	list_display =[field.name for field in blog._meta.fields]