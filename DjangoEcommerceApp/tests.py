from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import MyModel

class MyModelTest(TestCase):
    def setUp(self):
        # Test verilerini buraya ekliyoruz
        MyModel.objects.create(name='Test Item', description='Test description')

    def test_model_str(self):
        item = MyModel.objects.get(name='Test Item')
        self.assertEqual(str(item), 'Test Item')

    def test_view_status_code(self):
        response = self.client.get(reverse('my_view_url_name'))
        self.assertEqual(response.status_code, 200)

    def test_model_save(self):
        item = MyModel.objects.create(name='New Item', description='Another test item')
        self.assertEqual(MyModel.objects.count(), 2)

    def test_form_valid(self):
        response = self.client.post(reverse('my_form_url'), {'field_name': 'valid_data'})
        self.assertEqual(response.status_code, 302)  # Redirects after successful form submission
