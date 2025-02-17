from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profissional, Consulta
from django.utils import timezone

class ProfissionalTests(APITestCase):
    def test_create_profissional(self):
        url = '/api/profissionais/'
        data = {
            'nome': 'Dr. João',
            'profissao': 'Médico',
            'endereco': 'Rua X, 123',
            'contato': '987654321',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ConsultaTests(APITestCase):
    def test_create_consulta(self):
        profissional = Profissional.objects.create(
            nome='Dr. João', profissao='Médico', endereco='Rua X, 123', contato='987654321')
        url = '/api/consultas/'
        data = {
            'data': timezone.now().isoformat(),
            'profissional': profissional.id,
            'paciente_nome': 'Paciente 1'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
