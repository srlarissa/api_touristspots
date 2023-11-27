from django.contrib import admin
from .models import Comment
from .actions import mass_reprove_comment, mass_approve_comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['username','date','approved']
    actions = [mass_reprove_comment, mass_approve_comment]

admin.site.register(Comment, CommentAdmin)