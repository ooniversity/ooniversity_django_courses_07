from django.test import TestCase
from courses.models import Course

class CoursesListTest(TestCase):
    def test_response(self):
        from django.test import Client
        client = Client()

        response = client.get('/')
        self.assertEqual(response.status_code, 200)

class CoursesDetailTest(TestCase):
    def test_course_create(self):
        course1 = Course.objects.create(
            name = 'Course1',
            short_description = 'test',
            description = '1',
        )
        self.assertEqual(Course.objects.all().count(), 1)