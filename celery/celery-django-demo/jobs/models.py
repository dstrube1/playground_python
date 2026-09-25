from django.db import models


class Job(models.Model):
    input_text = models.TextField()

    status = models.CharField(
        max_length=20,
        default="PENDING",
    )

    result = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Job {self.id} - {self.status}"