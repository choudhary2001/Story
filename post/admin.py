from django.contrib import admin
from post.models import Post, Tag, Follow, Stream, contact

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(contact)

