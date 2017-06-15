from django.test import TestCase, Client
from students.models import Student
from datetime import date


class StudentsListTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Students list')

    def test_add_student(self):
        Student.objects.create(
            name='John',
            surname='Doe',
            date_of_birth=date(1234, 5, 10),
            email='test@test.com',
            phone='456546346',
            address='Alabama',
            skype='test'
        )
        self.assertEqual(Student.objects.all().count(), 1)
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_remove_student(self):
        student = Student.objects.create(
            name='John',
            surname='Doe',
            date_of_birth=date(1234, 5, 10),
            email='test@test.com',
            phone='456546346',
            address='Alabama',
            skype='test'
        )
        self.assertEqual(Student.objects.all().count(), 1)
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        response = self.client.get('/students/remove/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Do you want to remove student: John Doe ?')
        student.delete()
        self.assertEqual(Student.objects.all().count(), 0)

    def test_add_many_students(self):
        Student.objects.create(
            name='John',
            surname='Doe',
            date_of_birth=date(1234, 5, 10),
            email='test@test.com',
            phone='456546346',
            address='Alabama',
            skype='test'
        )
        Student.objects.create(
            name='Elon',
            surname='Musk',
            date_of_birth=date(2312, 1, 4),
            email='test@test.com',
            phone='456546346',
            address='Alabama',
            skype='test'
        )
        Student.objects.create(
            name='Brad',
            surname='Pitt',
            date_of_birth=date(2000, 8, 5),
            email='test@test.com',
            phone='456546346',
            address='Alabama',
            skype='test'
        )
        self.assertEqual(Student.objects.all().count(), 3)
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertContains(response, 'Elon Musk')
        response = self.client.get('/students/?page=2')
        self.assertContains(response, 'Brad Pitt')

    def test_no_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No students')
