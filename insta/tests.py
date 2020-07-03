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