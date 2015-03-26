from django.db import models


class Bicycle(models.Model):

    MAINTENANCE=(
        (1, 'Ready'),
        (2, 'Broken light'),
        (3, 'Broken heavily'),
        (4, 'Stolen'),
        (5, 'In repair'),
        (6, 'Unknown'),
    )
    FRAME = (
        (1, 'Fixie'),
        (2, 'Mountain'),
        (3, 'Road'),
        (4, 'High Nelly'),
        (5, 'Dutch'),
        (6, 'Tricycle'),
        (7, 'Tandem'),
        (99, 'Unknown'),
    )
    GENDER = (
        (1, "Ladies"),
        (2, "Gents"),
        (3, "Child"),
        (4, "Uni"),
    )
    SIZE = (
        (1, "XS"),
        (2, "S"),
        (3, "M"),
        (4, "L"),
        (5, "XL"),
        (99, 'Unknown'),
    )
    title = models.CharField(u"bicycle title", max_length=60, default='')  # bicycle title
    type_make = models.CharField('bicycle manufacturer', max_length=20, default='', blank=True)  # bicycle manufacturer
    type_model = models.CharField('manufacturer model', max_length=20, default='', blank=True)  # manufacturer model
    type_frame = models.IntegerField('frame type', default=1, max_length=2, choices=FRAME)  # frame type = road/mountain/fixie/etc
    type_gender = models.IntegerField('gender type', default=1, max_length=2, choices=GENDER)  # male/fem/uni/child
    type_height = models.IntegerField('height category', default=1, max_length=2, choices=SIZE)  # depend on frame/gender will be sets of sizes
    description = models.TextField('text description', default='default description')  # text description of the bike
    available = models.NullBooleanField(default=False)  # available or in use right now
    images = models.CharField('bike image for web', max_length=256, default='')  # bike image for web
    status = models.IntegerField('maintenance status', default=0, max_length=2, choices=MAINTENANCE)  # technical status - new, worn, to maintenance etc.
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

    title = models.CharField('Client title', max_length=10, choices=TITLES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.title + ' ' + self.first_name + ' ' + self.last_name


class Order(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    days = models.IntegerField(default=0)
    hours_above_days = models.IntegerField(default=0)
    client = models.ForeignKey(Client, verbose_name="ordered by")
    bicycle = models.ForeignKey(Bicycle, verbose_name="ordered bicycle")
    paid = models.NullBooleanField(default=False)
    invoiced = models.NullBooleanField(default=False)
    price = models.FloatField(default=0.0)  # on order create price will be calculated depending on order date/days/value

    def __str__(self):
        return str(self.id) + ' ' + self.client + ' ' + self.bicycle

