from django.test import TestCase
from .models import Student, Course
from django.test import Client

class StudentsListTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_download_empty_page(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']),0)
        self.assertContains(response, "No students are available.")
        self.assertFalse(response.context['is_paginated'])

    def test_page_with_student(self):
        student = Student.objects.create(name='1',surname='11',email='s@mail.com',
                                         phone='123',address='m',skype='k')
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 1)
        self.assertFalse(response.context['is_paginated'])


    def test_student(self):
        student = Student.objects.create(name='1', surname='11', email='s@mail.com', phone='123', address='m',
                                         skype='k')
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 1)
        self.assertFalse(response.context['is_paginated'])
        self.assertContains(response,"Delete",count=1)
        self.assertContains(response,"Edit",count=1)

    def test_page_with_students(self):
        student = Student.objects.create(name='1', surname='11', email='s@mail.com', phone='123', address='m',
                                         skype='k')
        student = Student.objects.create(name='2', surname='11', email='s@mail.com', phone='123', address='m',
                                         skype='k')
        student = Student.objects.create(name='3', surname='11', email='s@mail.com', phone='123', address='m',
                                         skype='k')
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.all().count(), 3)
        self.assertTrue(response.context['is_paginated'])
        self.assertContains(response,"Delete")
        self.assertContains(response,"Edit",count=2)

    def test_page(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Our students")
        self.assertContains(response, "Add new student")
        self.assertNotContains(response,"Delete")
        self.assertNotContains(response,"Edit")


class StudentsDetailTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.student = Student.objects.create(name='1', surname='11', email='s@mail.com', phone='123', address='m',
                                         skype='k')

    def test_invalid_student_id(self):
        response = self.client.get('/students/4/')
        self.assertEqual(response.status_code, 404)

    def test_valid_student_id(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['student'], self.student)

    def test_student_without_course(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['student'], self.student)
        self.assertContains(response, "Student doesn't have courses")

    def test_student(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['student'], self.student)
        self.assertContains(response, self.student.name)
        self.assertContains(response, self.student.surname)


    def test_page(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Courses")













# Create your tests here.
