from django.test import TestCase


# # Create your tests here.


class testHome(TestCase):

    class test_index(TestCase):
        def test_get_index(self):
            response = self.client.get('')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html')
