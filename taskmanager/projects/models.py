from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'Planning'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('on_hold', 'On Hold')
        ],
        default='planning'
    )
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_status_badge_color(self):
        status_colors = {
            'planning': 'secondary',
            'in_progress': 'primary',
            'completed': 'success',
            'on_hold': 'warning'
        }
        return status_colors.get(self.status, 'secondary')
