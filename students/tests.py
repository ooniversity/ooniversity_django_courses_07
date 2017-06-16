from django.test import TestCase
from students.models import Student
import datetime


class StudentsListTest(TestCase):
    def test_response(self):
        from django.test import Client
        client = Client()

        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)


class StudentsDetailTest(TestCase):
    def test_student_create(self):
        student1 = Student.objects.create(
            name = 'Student1',
            surname = 'Test',
            date_of_birth = datetime.date.today(),
        )
        self.assertEqual(Student.objects.all().count(), 1)