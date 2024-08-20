from django.contrib import admin

from rss.models import Feed, BaseLinks


class AdminFeed(admin.ModelAdmin):
    list_display = ('title', 'base_link__name', 'created_at')
    readonly_fields = ('created_at',)


class AdminBaseLinks(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Feed, AdminFeed)
admin.site.register(BaseLinks, AdminBaseLinks)
