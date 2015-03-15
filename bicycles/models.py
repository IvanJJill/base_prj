from django.db import models


class Bicycle(models.Model):
    title = models.CharField(max_length=200)  # bicycle title
    type_frame = models.IntegerField(default=1)  # frame type = road/mountain/fixie/etc
    type_gender = models.IntegerField(default=1)  # male/fem/child
    type_height = models.IntegerField(default=1)  # height category - depend on frame/gender will be sets of sizes
    description = models.TextField()  # text description of the bike. in html
    available = models.BinaryField()  # available or in use right now
    # occupied_order = models.ForeignKey()  # order id that the bike is occupied now
    image = models.ImageField()  # bike image for web
    status = models.IntegerField(default=0)  # technical status - new, worn, to maintenance etc.
