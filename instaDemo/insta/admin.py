from django.contrib import admin
from insta.models import Post, InstaUser, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)