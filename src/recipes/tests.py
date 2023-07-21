from django.test import TestCase
from .models import Recipe


# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name="Tea",
            cooking_time=5,
            difficulty="Easy",
            ingredients="Tea Leaves, Water, Sugar",
        )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_recipe_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("cooking_time").verbose_name
        self.assertEqual(field_label, "cooking time")

    def test_recipe_difficulty(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("difficulty").verbose_name
        self.assertEqual(field_label, "difficulty")

    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("ingredients").verbose_name
        self.assertEqual(field_label, "ingredients")

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)

    def test_recipe_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("ingredients").max_length
        self.assertEqual(max_length, 255)
