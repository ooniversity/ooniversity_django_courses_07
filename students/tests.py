from django.test import TestCase
from students.models import Student
from courses.models import Course


class CoursesDetailTest(TestCase):

    def test_student_create(self):
        student = create_student()
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student_detail(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student = create_student()
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_student_edit(self):
        student = create_student()
        response = self.client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/students/remove/1/')
        self.assertEqual(response.status_code, 200)

    def test_student_content(self):
        student = create_student()
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Human Old')

    def test_student_in_course(self):
        student = create_student()
        course = create_course()
        student.courses.add(course)
        response = self.client.get('/students/?course_id=1')
        self.assertContains(response, 'Old Human')


def create_student():
    student = Student.objects.create(
        name = 'Human',
        surname = 'Old',
        date_of_birth = '2017-10-10',
        email = '123@mail.com',
        phone = '89999999999',
        address = 'qwerty',
        skype = 'qwerty')
    return student

def create_course():
    course = Course.objects.create(
        name = 'ABC',
        short_description = 'Web Qwerty',
        description = 'qwerty')
    return course