from django.test import TestCase

# Test of the booking view


class test_booking(TestCase):

    def test_get_booking(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking.html')
