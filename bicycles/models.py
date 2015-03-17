from django.db import models


class Bicycle(models.Model):
    title = models.CharField("bicycle title", max_length=60)  # bicycle title
    type_make = models.CharField('bicycle manufacturer', max_length=20)  # bicycle manufacturer
    type_model = models.CharField('manufacturer model', max_length=20)  # manufacturer model
    type_frame = models.IntegerField('frame type', default=1)  # frame type = road/mountain/fixie/etc
    type_gender = models.IntegerField('gender type', default=1)  # male/fem/uni/child
    type_height = models.IntegerField('height category', default=1)  # height category - depend on frame/gender will be sets of sizes
    description = models.TextField('text description', )  # text description of the bike. in html
    available = models.BinaryField('availability', )  # available or in use right now
    # occupied_order = models.ForeignKey(Order)  # order id that the bike is occupied now
    image = models.CharField('bike image for web', max_length=256)  # models.ImageField()  # bike image for web
    status = models.IntegerField('maintenance status', default=0)  # technical status - new, worn, to maintenance etc.
    value = models.FloatField('Value in money', )  # bike value in f.ex. EUR to calculate the price

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
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    days = models.IntegerField()
    hours_above_days = models.IntegerField()
    client = models.ForeignKey(Client, verbose_name="ordered by")
    bicycle = models.ForeignKey(Bicycle, verbose_name="ordered bicycle")
    payed = models.BinaryField()
    invoiced = models.BinaryField()
    price = models.FloatField()  # on order create price will be calculated depending on order date/days/value

