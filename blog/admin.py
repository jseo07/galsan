from django.contrib import admin
from .models import Post
# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)

admin.site.register(Post,RatingAdmin)

