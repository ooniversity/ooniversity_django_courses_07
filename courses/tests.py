from django.test import TestCase
from .models import Course

class CourseTests(TestCase):

    def test_course_create(self):
        course1 = Course.objects.create(name='pybursa',
                                        short_description='web dev')
        self.assertEqual(Course.objects.all().count(),1)

    def test_pages(self):
        from django.test import Client
        client = Client()

        response = client.get('/course/1/')
        self.assertEqual(response.status_code,404)

        Course.objects.create(name="pybursa",short_description="description")
        response = client.get('/course/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'pybursa')