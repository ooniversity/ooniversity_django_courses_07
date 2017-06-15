from django.test import TestCase
from .models import Student
from django.test import Client
from datetime import date

def create_student(name):
    return Student.objects.create(name=name,
                           surname='Ivanov',
                           date_of_birth=date(1998,5,1),
                           email='test@gmail.com',
                           phone='+38082932',
                           address='Киев, ул. Пушкина, д. 24',
                           skype='test skype')

class StudentsListTest(TestCase):
    def test_list_200(self):
        student = create_student('Petrosyan')
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
    def test_content(self):
        student = create_student('Petrosyan')
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Petrosyan')
    def test_counts(self):
        create_student('Petrosyan')
        self.assertEqual(Student.objects.all().count(), 1)
    def test_correctrly_template_list(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Список студентов')
    def test_count_sd(self):
        create_student('Petrosyan')
        create_student('Petrosyan')
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Petrosyan',2)

class StudentsDetailTest (TestCase):
    def test_detail(self):
        student = create_student('Vasya')
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
    def test_404(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
    def test_name(self):
        student = create_student('Vasya')
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Vasya')
    def test_surname(self):
        student = create_student('Vasya')
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Vasya')
    def test_skype(self):
        student = create_student('Vasya')
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'test skype')