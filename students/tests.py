from django.test import TestCase
from students.models import Student
import datetime

def student_create():
    student = Student.objects.create(
        name='Student',
        surname='Test',
        date_of_birth=datetime.date.today(),
        email='example@example.com',
        phone='1111111',
        address='Some name street',
        skype='example',
    )
    return student


class StudentsListTest(TestCase):
    def test_students_list_response(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_students_create(self):
        response = self.client.get('/students/add/')
        self.assertEqual(response.status_code, 200)

    def test_students_list_with_5_students(self):
        for i in range(5):
            student = student_create()
        self.assertEqual(Student.objects.all().count(), 5)

    def test_students_edit(self):
        student = student_create()
        response = self.client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)

    def test_students_list(self):
        student = student_create()
        response = self.client.get('/students/1/')
        self.assertContains(response, student.name)
        self.assertContains(response, student.surname)
        self.assertContains(response, student.skype)


class StudentsDetailTest(TestCase):
    def test_student_create(self):
        student = student_create()
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student_detail(self):
        student = student_create()
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_student_fullname(self):
        student = student_create()
        self.assertEqual(student.fullname, 'Student Test')

    def test_student_info(self):
        student = student_create()
        response = self.client.get('/students/1/')
        self.assertContains(response, student.name)
        self.assertContains(response, student.surname)
        self.assertContains(response, student.email)

    def test_student_not_exist(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

