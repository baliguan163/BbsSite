from django.contrib import admin
from . models  import bbs,bbs_user,comment,category

# Register your models here.

class UserAmdin(admin.ModelAdmin):
	list_display = ('user_name','user_nice','user_passwd','user_signature','user_photo')
	list_editable = ('user_photo','user_passwd','user_signature','user_photo')
	list_filter = ('user_name',)
	search_fields = ('user_name',)

class CategoryAmdin(admin.ModelAdmin):
	list_display = ('name','admin')
	list_editable = ('name','admin')

class CommentAmdin(admin.ModelAdmin):
	list_display = ('content','uesr_id','bbs_id')
	list_editable = ('content','uesr_id','bbs_id')


class BbsAmdin(admin.ModelAdmin):
	list_display = ('title','summary','content','category','view_count','comment_count','author','ranking','publish_date','modify_date')
	#list_editable = ('title','summary','content')
	list_filter = ('publish_date',)

admin.site.register(bbs_user,UserAmdin)
admin.site.register(category,CategoryAmdin)
admin.site.register(bbs,BbsAmdin)
admin.site.register(comment,CommentAmdin)



