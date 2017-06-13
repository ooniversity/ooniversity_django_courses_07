from django.test import TestCase
from courses.models import Course, Lesson


class CoursesListTest(TestCase):

    def test_course_create(self):
        create_course()
        self.assertEqual(Course.objects.all().count(), 1)

    def test_add_lesson(self):
        course = create_course()
        lesson = create_lesson(course)
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_course_list1(self):
        create_course()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_course_list2(self):
        create_course()
        response = self.client.get('/')
        self.assertContains(response, 'ABC')

    def test_course_list3(self):
        create_course()
        response = self.client.get('/')
        self.assertContains(response, 'Web Qwerty')

    def test_course_list4(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class CoursesDetailTest(TestCase):

    def test_course_detail1(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_course_detail2(self):
        create_course()
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_detail3(self):
        create_course()
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'ABC')

    def test_course_detail4(self):
        create_course()
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'qwerty')

    def test_course_detail_lesson(self):
        course = create_course()
        lesson = create_lesson(course)
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'lesson1')

    def test_course_edit(self):
        course = create_course()
        create_lesson(course)
        response = self.client.get('/courses/edit/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/courses/remove/1/')
        self.assertEqual(response.status_code, 200)


def create_course():
    course = Course.objects.create(
        name = 'ABC',
        short_description = 'Web Qwerty',
        description = 'qwerty')
    return course

def create_lesson(course=None):
    lesson = Lesson.objects.create(
        subject = 'lesson1',
        description = 'qwerty',
        course = course,
        order = 1)
    return lesson