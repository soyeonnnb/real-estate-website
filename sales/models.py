import random

from django.db import models
from core.models import TimeStampedModel
from django.core.validators import MinValueValidator


class Sale(TimeStampedModel):

    """Sale Model"""

    TYPE_SALE = "sale"
    TYPE_JEONSE = "jeonse"
    TYPE_MONTHLY = "monthly"
    TYPE_CHOICES = (
        (TYPE_SALE, "Sale"),
        (TYPE_JEONSE, "Jeonse"),
        (TYPE_MONTHLY, "Monthly"),
    )

    complex_sub = models.ForeignKey(
        "complexes.ComplexSub",
        related_name="sale",
        on_delete=models.SET_NULL,
        null=True,
    )
    address = models.TextField(blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=7)
    deposit = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(0)]
    )
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    floor = models.IntegerField()
    loan = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    administrative_expense = models.IntegerField(validators=[MinValueValidator(0)])
    available_date = models.DateField()
    description = models.TextField()
    one_description = models.TextField()
    is_sold = models.BooleanField()

    def first_image(self):
        images = self.sale_image.all()
        return images[0]


def sale_directory_path(instance, filename):
    n = random.randint(10000, 99999)
    return f"sale/sale_{instance.id}/{filename}-{n}"


class SaleImage(TimeStampedModel):

    """Sale Image Model"""

    sale = models.ForeignKey(Sale, related_name="sale_image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=sale_directory_path)
    description = models.TextField()
