from django.db import models

# Create your models. fields are for NEM13 for 250
class Meter(models.Model):
    nmi = models.CharField(max_length=100)   #field2
    meter_serial_number = models.CharField(max_length=100)   #field 7
    #reading = models.IntegerField()     #field 14
    #reading_datetime = models.DateTimeField()   #field 15
    reading = models.CharField(max_length=100)    #field 14
    reading_datetime = models.CharField(max_length=100)   #field 15
    file_name = models.CharField(max_length=100)  # filename

    def __str__(self):
        return self.nmi