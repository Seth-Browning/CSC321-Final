from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ReportType(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Report(models.Model):

    reporting_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="reports_made")

    # Generic Relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    reported_object = GenericForeignKey("content_type", "object_id")

    report_type = models.ForeignKey(ReportType, null=True, on_delete=models.SET_NULL)

    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Moderation fields
    is_resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolved_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="reports_resolved")

    def __str__(self):
        return f"Report on {self.content_type.model} (id={self.object_id})"