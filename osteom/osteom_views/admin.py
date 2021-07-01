from django.contrib import admin

# Register your models here.
from .models import Tag, Feedback, Posts, Certificate, Bio, Jobs, ServicePrices, BlogAbout


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']

    class Meta:
        model = Tag


class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'is_urgent', 'get_tags']
    search_fields = ['title', 'content']
    list_filter = ['tags', 'date_created', 'is_urgent']

    class Meta:
        model = Posts


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'time', 'is_visible']
    search_fields = ['name', 'surname']
    list_filter = ['time', 'is_visible']

    class Meta:
        model = Feedback


class CertficateAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']
    search_fields = ['title']
    list_filter = ['title', 'date_created']

    class Meta:
        model = Certificate


class JobsAdmin(admin.ModelAdmin):
    list_display = ['address', 'work_time', 'phones', 'date_created']
    search_fields = ['phone']
    list_filter = ['date_created']

    class Meta:
        model = Jobs


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'free']
    search_fields = ['title']
    list_filter = ['price', 'free']

    class Meta:
        model = ServicePrices


admin.site.register(Posts, PostsAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Certificate, CertficateAdmin)
admin.site.register(Bio)
admin.site.register(Jobs, JobsAdmin)
admin.site.register(ServicePrices, ServiceAdmin)
admin.site.register(BlogAbout)
