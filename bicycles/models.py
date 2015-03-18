from django.db import models


class Bicycle(models.Model):
    title = models.CharField(u"bicycle title", max_length=60, default='')  # bicycle title
    type_make = models.CharField('bicycle manufacturer', max_length=20, default='')  # bicycle manufacturer
    type_model = models.CharField('manufacturer model', max_length=20, default='')  # manufacturer model
    type_frame = models.IntegerField('frame type', default=1)  # frame type = road/mountain/fixie/etc
    type_gender = models.IntegerField('gender type', default=1)  # male/fem/uni/child
    type_height = models.IntegerField('height category', default=1)  # depend on frame/gender will be sets of sizes
    description = models.TextField('text description', default='default desciption')  # text description of the bike
    available = models.BinaryField('availability', default=True)  # available or in use right now
    images = models.CharField('bike image for web', max_length=256, default='')  # bike image for web
    status = models.IntegerField('maintenance status', default=0)  # technical status - new, worn, to maintenance etc.
    value = models.FloatField('value in money', default=0.0)  # bike value in f.ex. EUR to calculate the price

    """to return a name of itself when called from anywhere"""
    def __str__(self):
        return self.title


class Client(models.Model):
    TITLES = (
        ('Mister', 'Mr'),
        ('Mistress', 'Mrs'),
        ('Miss', 'Ms'),
    )

    title = models.CharField('Client title', max_length=1, choices=TITLES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=12, blank=True)


class Order(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    days = models.IntegerField(default=0)
    hours_above_days = models.IntegerField(default=0)
    client = models.ForeignKey(Client, verbose_name="ordered by")
    bicycle = models.ForeignKey(Bicycle, verbose_name="ordered bicycle")
    payed = models.BinaryField(default=False)
    invoiced = models.BinaryField(default=False)
    price = models.FloatField(default=0.0)  # on order create price will be calculated depending on order date/days/value

