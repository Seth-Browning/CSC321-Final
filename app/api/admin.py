from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Report, ReportType

# Register your models here.

# admin.site.register(Report)
admin.site.register(ReportType)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "report_type",
        "reporting_user",
        "get_reported_object",
        "created_at",
        "is_resolved",
    )
    list_filter = ("report_type", "content_type", "is_resolved")
    search_fields = ("description",)

    def get_reported_object(self, obj):
        if obj.reported_object:
            # Create a link to the reported object's admin page
            url = reverse(
                f"admin:{obj.content_type.app_label}_{obj.content_type.model}_change",
                args=[obj.object_id]
            )
            return format_html('<a href="{}">{}</a>', url, str(obj.reported_object))
        return "(deleted)"
    
    get_reported_object.short_description = "Reported Object"
