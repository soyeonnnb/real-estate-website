from django.db import models
from core.models import TimeStampedModel
import random


class Category(TimeStampedModel):

    """Category Model"""

    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Complex(TimeStampedModel):

    """Complex Model"""

    HEATING_CENTER = "center"
    HEATING_LOCAL = "local"
    HEATING_PARTI = "parti"
    HEATING_CHOICES = (
        (HEATING_CENTER, "Center"),
        (HEATING_LOCAL, "Local"),
        (HEATING_PARTI, "Parti"),
    )

    category = models.ForeignKey(
        Category, related_name="complex", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    parking = models.IntegerField()
    heating = models.CharField(choices=HEATING_CHOICES, max_length=6)
    approval_use = models.DateField()
    company = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()

    def __str__(self):
        return self.name

    # 면적 종류
    def get_areas(self):
        return self.complex_area.all()

    # 세대 수
    def get_apartment(self):
        all_areas = self.complex_area.all()
        all_apartments = 0
        for area in all_areas:
            subs = area.get_complex_sub()
            for sub in subs:
                all_apartments += sub.apartment
        return all_apartments

    class Meta:
        verbose_name_plural = "Complexes"


class ComplexArea(TimeStampedModel):

    """Complex Area Model"""

    complex = models.ForeignKey(
        Complex, related_name="complex_area", on_delete=models.CASCADE
    )
    supply_area = models.FloatField()
    exclusive_private_area = models.FloatField()
    room = models.IntegerField()
    bath = models.IntegerField()

    def __str__(self):
        return f"{self.complex} - {round(self.exclusive_private_area, 3)}"

    def get_complex_sub(self):
        return self.complex_sub.all()


class ComplexSub(TimeStampedModel):

    """Sub Complex Model"""

    complex_area = models.ForeignKey(
        ComplexArea, related_name="complex_sub", on_delete=models.CASCADE
    )
    building = models.IntegerField(null=False, blank=False)
    floor = models.IntegerField(null=False, blank=False)
    apartment = models.IntegerField(null=False, blank=False)
    facing = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.complex_area.complex} - {self.building}"


def complex_directory_path(instance, filename):
    n = random.randint(10000, 99999)
    return f"complex/complex_{instance.id}/{filename}-{n}"


class ComplexImage(TimeStampedModel):

    """Complex Image Model"""

    complex = models.ForeignKey(
        Complex, related_name="complex_image", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=complex_directory_path)
    description = models.TextField()
