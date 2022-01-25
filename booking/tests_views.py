from django.test import TestCase
# from django.urls import reverse, resolve
# from .views import booking

# Create your tests here.
class test_booking(TestCase):

    def test_get_booking(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking.html')

        # url = reverse("booking") # or whatever you have for name= in the url path in urls.py

        # response = self.client.get(url)
        # print(response)
        # print(url)