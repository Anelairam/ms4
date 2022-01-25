from django.test import TestCase

# # Create your tests here.

class testBooknow(TestCase):

    class test_booknow(TestCase):
        def test_get_booking(self):
            response = self.client.get('/booknow/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'booknow.html')

