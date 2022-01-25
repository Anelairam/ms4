from django.test import TestCase
from django.urls import reverse
from .views import info

# # Create your tests here.

class testHome(TestCase):

    class test_index(TestCase):
        def test_get_index(self):
            # url = reverse("info") # or whatever you have for name= in the url path in urls.py
            # print(url)
            response = self.client.get('')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html')