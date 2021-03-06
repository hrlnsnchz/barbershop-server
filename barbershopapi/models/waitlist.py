from django.db import models
from django.utils.timezone import now

class Waitlist(models.Model):

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    barber = models.ForeignKey("Barber", on_delete=models.CASCADE)
    time = models.DateTimeField(default=now)
    is_served = models.BooleanField(default=False)
    waitlist_services = models.ManyToManyField("Service", related_name="barber_waitlists")
    # spot_in_line = models.IntegerField(default=0) 