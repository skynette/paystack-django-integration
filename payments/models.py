from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import secrets

# Create your models here.
class UserWallet(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    currency = models.CharField(max_length=50, default='NGN')
    created_at = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.user.__str__()

class Payment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	amount = models.PositiveIntegerField()
	ref = models.CharField(max_length=200)
	email = models.EmailField()
	verified = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-date_created',)

	def __str__(self):
		return f"Payment: {self.amount}"

	def save(self, *args, **kwargs):
		while not self.ref:
			ref = secrets.token_urlsafe(50)
			object_with_similar_ref = Payment.objects.filter(ref=ref)
			if not object_with_similar_ref:
				self.ref = ref

		super().save(*args, **kwargs)
	
	