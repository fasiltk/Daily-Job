from django.db import models
from authsystem.models import Labour, Customer
from django.utils import timezone

class ChatMessage(models.Model):
    labour = models.ForeignKey(Labour, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sender_type = models.CharField(
        max_length=10,
        choices=[('labour', 'Labour'), ('customer', 'Customer')]
    )
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender_type} → {self.message[:20]}"
