from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

# Default user models for the app
USER = get_user_model()


class Task(models.Model):
    STATUS = (
        ("P", "Pending"),
        ("I_P", "In Progress"),
        ("C", "Completed"),
    )
    """Task status choices"""
    PRIORITY = (
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
    )
    """Task priority choices"""
    title = models.CharField(max_length=200)
    """Task name"""
    description = models.TextField(blank=True)
    """Task description"""
    owner = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="tasks")
    """Task dooer"""
    status = models.CharField(max_length=3, choices=STATUS, default="P")
    """Task status"""
    priority = models.CharField(max_length=1, choices=PRIORITY, default="M")
    """Priority of the task"""
    due_date = models.DateTimeField(null=True)
    """Deadline of the task"""
    completed_at = models.DateTimeField(null=True, blank=True)
    """Time of completion of the task"""
    created_at = models.DateTimeField(auto_now_add=True)
    """Date of creation of the task"""
    updated_at = models.DateTimeField(auto_now=True)
    """Last Date the task was modified or tampered"""

    class Meta:
        indexes = [
            models.Index(fields=["owner", "status"]),
            models.Index(fields=["owner", "due_date"]),
        ]
        ordering = ["-created_at"]
    
    @property
    def is_archived(self) -> bool:
        """Checking whether the task time of completion was attained"""
        # We check if the fields completed at and due_date are emptly
        if self.completed_at is not None and self.due_date is not None:
            # if the value of complete time is earlier than the start date we return true
            if self.completed_at < self.due_date:
                return True
        # if not we return false
        return False

    def save(self, *args, **kwargs):
        if self.status == "C" and self.completed_at is None:
            self.completed_at = timezone.now()
        if self.status != "C":
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.owner})"
