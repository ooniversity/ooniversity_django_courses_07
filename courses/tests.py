from django.test import TestCase, Client
from courses.models import Course


class CoursesListTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PyBursa')

    def test_add_course(self):
        Course.objects.create(
            name='PythonCourse',
            short_description='Short Python description',
            description='Python description'
        )
        self.assertEqual(Course.objects.all().count(), 1)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PythonCourse'.upper())

    def test_remove_course(self):
        course = Course.objects.create(
            name='PythonCourse',
            short_description='Short Python description',
            description='Python description'
        )
        self.assertEqual(Course.objects.all().count(), 1)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PythonCourse'.upper())
        response = self.client.get('/courses/remove/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Do you want to remove course: PythonCourse ?')
        course.delete()
        self.assertEqual(Course.objects.all().count(), 0)

    def test_add_many_courses(self):
        Course.objects.create(
            name='PythonCourse',
            short_description='Short Python description',
            description='Python description'
        )
        Course.objects.create(
            name='RubyCourse',
            short_description='Short Ruby description',
            description='Ruby description'
        )
        Course.objects.create(
            name='C++Course',
            short_description='Short C++ description',
            description='C++ description'
        )
        self.assertEqual(Course.objects.all().count(), 3)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PythonCourse'.upper())
        self.assertContains(response, 'RubyCourse'.upper())
        self.assertContains(response, 'Course'.upper())

    def test_no_courses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No courses')
