from django.db import models

# Create your models here.
class Tenant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=20)
    id_number = models.IntegerField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Room(models.Model):
    room_number = models.IntegerField(max_length=20)
    room_type = models.CharField(max_length=50)
    rent_amount = models.IntegerField(max_length=20)

    def __str__(self):
        return self.room_number

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.tenant.first_name + " " + self.tenant.last_name + " - " + str(self.room.room_number)
