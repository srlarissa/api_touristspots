def mass_reprove_comment(modeladmin, request, queryset):
    queryset.update(approved=False)

def mass_approve_comment(modeladmin, request, queryset):
    queryset.update(approved=True)


mass_reprove_comment.short_description = 'Reprove all comments'
mass_approve_comment.short_description = 'Approve all comments'

