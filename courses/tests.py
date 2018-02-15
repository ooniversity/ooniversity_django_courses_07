from django.test import TestCase
from .models import Course
from django.test import Client

class CoursesListTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_download_empty_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['courses_list']),0)

    def test_page_with_course(self):
        course = Course.objects.create(name='123',short_description='111',description='222')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.all().count(), 1)


    def test_course(self):
        course = Course.objects.create(name='123',short_description='111',description='222')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.all().count(), 1)
        self.assertContains(response,"Remove",count=1)
        self.assertContains(response,"Edit",count=1)

    def test_page_with_courses(self):
        course = Course.objects.create(name='123',short_description='111',description='222')
        course = Course.objects.create(name='123',short_description='111',description='222')
        course = Course.objects.create(name='123',short_description='111',description='222')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.all().count(), 3)
        self.assertContains(response,"Remove",count=3)
        self.assertContains(response,"Edit",count=3)

    def test_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add new course")
        self.assertNotContains(response,"Remove")
        self.assertNotContains(response,"Edit")


class CoursesDetailTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(name='123',short_description='111',description='222')

    def test_invalid_id(self):
        response = self.client.get('/courses/3/')
        self.assertEqual(response.status_code, 404)

    def test_course_without_lessons(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['course'], self.course)
        self.assertEqual(len(response.context['lesson_list']),0)

    def test_course_without_coach(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['course'], self.course)
        self.assertEqual(len(response.context['coach_list']),0)
        self.assertNotContains(response, "Coach")

    def test_course_without_assistant(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['course'], self.course)
        self.assertEqual(len(response.context['assistant_list']),0)
        self.assertNotContains(response, "Assistant")

    def test_page(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add lesson")
        self.assertContains(response, "Lessons")






















# Create your tests here.
