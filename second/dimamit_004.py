# from django.test import TestCase
# from myapp.models import Animal
#
#
# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")
#
#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         sel
# import factory
# from app.models import User
#
#
# class UserFactory(factory.Factory):
#     firstname = "John"
#     lastname = "Doe"
#
#     class Meta:
#         model = User
# На один класс можно создавать несколько объектов фабрик
#
# >>>john = UserFactory()
# <User: John Doe>
# >>>jack = UserFactory(firstname="Jack")
# <User: Jack Doe>
# Так же можно использовать разные фабрики в разных местах
#
# class EnglishUserFactory(factory.Factory):
#     class Meta:
#         model = User
#
#     firstname = "John"
#     lastname = "Doe"