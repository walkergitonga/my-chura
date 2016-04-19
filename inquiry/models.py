from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.
class Inquiry(models.Model):
    SERVICES = (
    ('CHURA PAYPAL TO M-PESA', 'Chura Paypal to M-PESA'),
    ('CHURA BUY AIRTIME', 'Chura Buy Airtime'),
    ('CHURA BUY DATA', 'Chura Buy Data'),
    ('CHURA BULK AIRTIME', 'Chura Bulk Airtime'),
    ('CHURA AIRTIME FOR CASH', 'Chura Airtime for Cash'),
    )

    DEPARTMENTS = (
        ('CUSTOMER CARE', 'Customer Care'),
        ('SALES', 'Sales'),
        ('DESIGN', 'Design'),
        ('DEVELOPMENT', 'Development'),
        ('MAINTENANCE', 'Maintenance'),
    )
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('RESOLVED', 'Resolved'),
    ]
    
    fullname     = models.CharField(max_length=50)
    phonenumber  = models.CharField(max_length=50)
    service      = models.CharField(max_length=50, choices=SERVICES)
    complaint    = models.CharField(max_length=500)
    department   = models.CharField(max_length=50, choices=DEPARTMENTS)
    status       = models.CharField(choices=STATUS_CHOICES, max_length=10, default='Pending')
    comment      = models.CharField(max_length=500, default='')
    date         = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "%s %s %s %s" % (self.fullname, self.service, self.complaint, self.department)