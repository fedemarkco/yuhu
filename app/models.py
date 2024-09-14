from django.db import models


class ModelTask(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(null=False)
    description = models.TextField(null=True)
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title
