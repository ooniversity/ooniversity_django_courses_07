from django.test import TestCase
from courses.models import Course, Lesson


def course_create():
    course = Course.objects.create(
        name='Course',
        short_description='Course description',
        description='1',
    )
    return course


def lesson_create(course = None):
    lesson = Lesson.objects.create(
        subject='Lesson',
        description='Lesson description',
        order=1,
        course=course,
    )
    return lesson


class CoursesListTest(TestCase):
    def test_courses_list_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_courses_list_content(self):
        response = self.client.get('/')
        self.assertIn(b'PyBursa', response.content)

    def test_courses_list_with_5_courses(self):
        for i in range(5):
            course = course_create()
        self.assertEqual(Course.objects.all().count(), 5)

    def test_courses_list_empty(self):
        course = course_create()
        Course.objects.filter(id=1).delete()
        self.assertEqual(Course.objects.all().count(), 0)

    def test_courses_list_context(self):
        response = self.client.get('/')
        self.assertContains(response, 'PyBursa')


class CoursesDetailTest(TestCase):
    def test_course_detail_response(self):
        course = course_create()
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_detail_render(self):
        course = course_create()
        response = self.client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_course_detail_create_lesson(self):
        course = course_create()
        lesson = lesson_create(course=course)
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_course_detail_context(self):
        course = course_create()
        response = self.client.get('/courses/1/')
        self.assertContains(response, course.name)

    def test_course_detail_not_exist(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
