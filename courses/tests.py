from django.test import TestCase, Client
from courses.models import Course, Lesson


def create_course(name):
    course = Course.objects.create(name=name,
                                   short_description='short_description Qwerty',
                                   description = 'description')
    return course


def create_lesson(subject, course=None):
    lesson = Lesson.objects.create(subject=subject,
                                   course=course,
                                   description='description',
                                   order=1)
    return lesson


class CoursesListTest(TestCase):
    def test_courses_create(self):
        course1 = Course.objects.create(name = 'PyBursa', short_description = 'short description')
        self.assertEqual(Course.objects.all().count(), 1)

    def test_pages(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(name='PyBursa', short_description='short description')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PyBursa')

    def test_courses_view_with_no_course(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'На данный момент нет активных курсов')
        self.assertQuerysetEqual(response.context['cour'], [])

    def test_courses_view_with_one_courses(self):
        create_course(name='Python')
        response = self.client.get('/')
        self.assertQuerysetEqual(response.context['cour'], ['<Course: Python>'])
        self.assertContains(response, "<a href='/courses/1/'>PYTHON</a>")
        self.assertContains(response, 'Изменить</a>')
        self.assertContains(response, 'Удалить</a>')

    def test_courses_view_with_3_courses(self):
        create_course(name='Python')
        create_course(name='Java')
        create_course(name='php')
        response = self.client.get('/')
        self.assertQuerysetEqual(response.context['cour'],
                                 ['<Course: Python>', '<Course: Java>', '<Course: php>'],
                                 ordered=False)


class CoursesDetailTest(TestCase):
    def test_create_lesson(self):
        course = create_course('Python')
        lesson = create_lesson(subject='Первый урок', course=course)
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_lesson_detail(self):
        course = create_course('Python')
        lesson = create_lesson(subject='Первый урок', course=course)
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'Первый урок')

    def test_lesson_detail_description(self):
        course = create_course('Python')
        lesson = create_lesson(subject='Первый урок', course=course)
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'description')

    def test_coach_assistant_lesson(self):
        course = create_course(name='Python')
        create_lesson(subject='Первый урок', course=course)
        create_lesson(subject='Второй урок', course=course)
        response = self.client.get('/courses/1/')
        if not course.coach or not course.assistant:
            self.assertContains(response, '<p>Преподаватель и Ассистент еще не назначены на данный курс</p>')
        else:
            self.assertContains(response, course.coach.user.first_name)
            self.assertContains(response, course.assistant.user.first_name)

    def test_one_course_view_with_2_lessons(self):
        course = create_course(name='Python')
        create_lesson(subject='Первый урок', course=course)
        create_lesson(subject='Второй урок', course=course)
        response = self.client.get('/courses/1/')
        self.assertEqual(response.context["object"], course)
        self.assertQuerysetEqual(response.context["lessons"],
                                 ['<Lesson: Первый урок>', '<Lesson: Второй урок>'],
                                 ordered=False)
        self.assertContains(response, 'Python')
