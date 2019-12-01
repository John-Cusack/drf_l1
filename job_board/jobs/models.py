from django.db import models


class JobOffer(models.Model):
    company_name = models.CharField(max_length=70)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=60)
    available = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name