from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class SocialMediaAccount(models.Model):
    SOCIAL_MEDIA_CHOICES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        # Add more social media platforms as needed
    )
    
    name = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CHOICES, unique=True)
    
    def __str__(self):
        return self.name

class ScamReport(models.Model):
    CATEGORY_CHOICES = (
        ('scam', 'Scam'),
        ('hack', 'Hack'),
        ('crack', 'Crack'),
    )
    
    REPORT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('submitted', 'Submitted'),
        ('resolved', 'Resolved'),
    )
    
    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    
    your_full_name = models.CharField(max_length=100)
    your_email = models.CharField(max_length=100)
    url = models.URLField()
    report_email = models.CharField(max_length=100, blank=True)
    report_phone = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField()
    report_status = models.CharField(max_length=10, choices=REPORT_STATUS_CHOICES, default='pending')
    aggregate_score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    location_country = models.CharField(max_length=100, blank=True)
    location_state = models.CharField(max_length=100, blank=True)
    location_city = models.CharField(max_length=100, blank=True)
    evidence = models.FileField(upload_to='scam_reports/', blank=True)
    severity_level = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='low')
    source = models.CharField(max_length=100, blank=True)
    investigator_notes = models.TextField(blank=True)
    action_taken = models.TextField(blank=True)
    feedback = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.category} Report for {self.url}"


class ScamReportAdmin(admin.ModelAdmin):
    list_display = ('category', 'description','your_full_name','timestamp')
    list_filter = ('category', 'your_full_name')
    search_fields = ('category', 'reported_url')


class ReportVote(models.Model):
    report = models.ForeignKey(ScamReport, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    is_upvote = models.BooleanField()

    class Meta:
        unique_together = ('report', 'ip_address')