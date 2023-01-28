from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

class TodoItem(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="New Todo Item")
    notes = models.TextField()
    next_step_owner = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    next_checkin = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
