from django.contrib import admin

from .models import Room, Topic, Message, User

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Room)
# Register your models here.
