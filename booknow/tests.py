from django.test import TestCase
from .forms import BookForm

# Create your tests here.

class TestBookForm(TestCase):

    def test_booked_time_is_required(self):
        form = BookForm({'booked_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('booked_time', form.errors.keys())
        self.assertEqual(form.errors['booked_time'[0]], 'This field is required.')

    def test_used_id_is_not_required(self):
        form = BookForm({'booked_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('booked_time', form.errors.keys())
        self.assertEqual(form.errors['booked_time'[0]], 'This field is required.')