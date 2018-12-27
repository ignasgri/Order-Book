# from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

turkey = (
    ('whole_turkey', 'WHOLE TURKEY'),
    ('boned_and_rolled', 'B + R'),
    ('boneed_rolled_stuffed', 'B + R + S'),
    ('boned_rolled_own_stuffing', 'B + R + OWN STUFFING'),
    ('crown', 'CROWN'),
    ('crown_boned_rolled', 'B + R CROWN'),
    ('crown_boned_rolled_stuffed', 'B + R + STUFFED'),
    ('turkey_breast', 'TURKEY BREAST'),
)

t_type = (
    ('farm_fresh', 'FARM FRESH'),
    ('free_range', 'FREE RANGE'),
    ('organic', 'ORGANIC'),
)

weight = (
    ('2kg', '2KG'),
    ('2_5kg', '2.5 KG'),
    ('3kg', '3KG'),
    ('3_5kg', '3.5KG'),
    ('4kg', '4kg'),
    ('4_5kg', '4.5KG'),
    ('5kg', '5KG'),
    ('5_5kg', '5.5KG'),
    ('6_5kg', '6.5KG'),
    ('7_5kg', '7.5KG'),
    ('8_5kg', '8.5KG'),
    ('9_5kg', '9.5KG'),
    ('10_5kg', '10.5KG'),
)

staff_initials = (
    ('tom', 'TOM'),
    ('mick', 'MICK'),
    ('chris', 'CHRIS'),
)

collection_date = (
    ('21', '21ST'),
    ('22', '22ND'),
    ('23', '23RD'),
    ('24', '24TH'),
    ('29', '29ND'),
    ('30', '30TH'),
    ('31', '31ST'),
)

class Turkey_Orders(models.Model):

    # author = models.ForeignKey('auth.User')
    create_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=254, default='')
    address = models.CharField(max_length=254, default='')
    phone_number = models.IntegerField(default='')
    turkey = models.CharField(max_length=20, choices=turkey, default='whole_turkey')
    t_type = models.CharField(max_length=20, choices=t_type, default='farm_fresh')
    weight = models.CharField(max_length=20, choices=weight, default='5_5kg')
    collection_date = models.CharField(max_length=20, choices=collection_date, default=24)
    staff_initials = models.CharField(max_length=10, choices=staff_initials, default='')
    comments = models.TextField()

    def publish(self):
        self.create_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name