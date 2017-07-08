from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'date_time')

admin.site.register(Article, ArticleAdmin)
