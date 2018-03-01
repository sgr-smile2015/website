from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'qq', 'source', 'consultant', 'content', 'status', 'date')
    list_filter = ('source', 'consultant', 'date')
    search_fields = ('qq', 'name')
    raw_id_fields = ('consult_course',)
    filter_horizontal = ('tags',)
    list_editable = ('status',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Tag)
admin.site.register(CustomerFollowUp)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(ClassList)
admin.site.register(CourseRecord)
admin.site.register(StudyRecord)
admin.site.register(Enrollment)
admin.site.register(Payment)
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(Menu)
