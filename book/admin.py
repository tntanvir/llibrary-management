from django.contrib import admin
from .models import book,borrow,BookComment
# Register your models here.

admin.site.register(book)
admin.site.register(borrow)
admin.site.register(BookComment)

