from django.db import models

difficulty_choices = (
    ("Easy", "easy"),
    ("Medium", "medium"),
    ("Intermediate", "intermediate"),
    ("Hard", "hard"),
)


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooking_time = models.PositiveIntegerField()
    difficulty = models.CharField(
        max_length=12, choices=difficulty_choices, default="Easy"
    )
    ingredients = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
