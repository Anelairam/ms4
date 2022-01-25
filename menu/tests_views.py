from django.test import TestCase
from django.urls import reverse, resolve
from .views import menu, add_item, edit_item, delete_item
from .models import menu_item

# then in your test:



# Create your tests here.
class test_Menu_template(TestCase):

    def test_get_menu(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')
        

    def test_get_add_item(self):
        response = self.client.get('/menu/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/add_item.html')

    def test_get_edit_item(self):
        item = menu_item.objects.create(title='Test title', components='Test comp', price=45, item_category=0)
        response = self.client.get(f'/menu/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/edit_item.html')


    def test_get_delete(self):
        item = menu_item.objects.create(title='Test title', components='Test comp', price=45, item_category=0)
        response = self.client.get(f'/menu/delete/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')

