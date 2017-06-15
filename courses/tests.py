from django.test import TestCase
from .models import Course
from django.test import Client

def create_course(name):
    return Course.objects.create(name=name, short_description='short desc', description='descript')

class CoursesListTest (TestCase):
    def test_list(self):
        course1 = create_course('pybursa')
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, course1.name.upper())
    def test_short_desc(self):
        course1 = create_course('pybursa')
        client = Client()
        response = client.get('/')
        self.assertContains(response, course1.short_description.title())
    def test_upper(self):
        course1 = create_course('pybursa')
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'p'.upper())
    def test_no_404(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_no_course(self):
        client = Client()
        response = client.get('/')
        not self.assertContains(response, 'p'.upper())

class CoursesDetailTest (TestCase):
    def test_200(self):
        course1 = create_course('pybursa')
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
    def test_404(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
    def test_name(self):
        course1 = create_course('pybursa')
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response,course1.name)
    def test_description(self):
        course1 = create_course('pybursa')
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response,course1.description[:32])
    def test_over(self):
        course1 = create_course('pybursa')
        client = Client()
        response = client.get('/courses/1/')
        not self.assertContains(response, course1.description)