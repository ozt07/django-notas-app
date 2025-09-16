from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):
    def test_basic_math(self):
        """Test básico de matemáticas"""
        self.assertEqual(1 + 1, 2)
    
    def test_home_page_status(self):
        """Test que verifica que la página principal carga correctamente"""
        response = self.client.get(reverse('lista_notas'))
        self.assertEqual(response.status_code, 200)
    
    def test_calculadora_page_status(self):
        """Test que verifica que la página de calculadora carga correctamente"""
        response = self.client.get(reverse('calculadora'))
        self.assertEqual(response.status_code, 200)