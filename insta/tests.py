from django.test import TestCase
from .models import Instalite,Image
# Create your tests here.

class InstaliteTestCase(TestCase):
    def setUp(self):
        self.cecilia = Instalite(first_name='Cecilia', last_name='Barasa', email='ceciheroku@gmail.com')
        
    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cecilia, Instalite))

    # testing the save method
    def test_save_method(self):
        self.cecilia.save_instalite()
        insta = Instalite.objects.all()
        self.assertTrue(len(insta) > 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.cecilia = Instalite(first_name='Cecilia', last_name='Barasa', email='ceciheroku@gmail.com')
        self.cecilia.save_instalite()

        self.new_image = Image(name='test image', image_caption='aight', likes='2', comment='Its good')
        self.new_image.save()

    def tearDown(self):
        Instalite.objects.all().delete()
        Image.objects.all().delete()    