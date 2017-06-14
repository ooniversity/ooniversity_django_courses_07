import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from students.models import Student
from courses.models import Course


def add_course(student, course):
    for item in course:
        course = Course.objects.create(name='Курс %s' % item, description='Описание курса по %s' % item)
        student.course.add(course)
    return student



def create_student(name, surname, course):
    student = Student.objects.create(name=name,
                                      surname=surname,
                                      date_of_birth=datetime.date(1986, 3, 25),
                                      address='Киев, ул. Артема, 6, кв 1',
                                      email='test@gmail.com',
                                      skype='test',
                                      phone='044111111')
    return student


class StudentsListTest(TestCase):
    def test_student_create(self):
        student = create_student('Иван', 'Иванов', 'Python')
        self.assertEqual(Student.objects.all().count(), 1)

    def test_students_view_with_no_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Пока-что нет ни одного студента")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_students_view_with_one_student(self):
        create_student(name='Иван', surname='Иванов', course=['Python'])
        response = self.client.get('/students/')
        self.assertQuerysetEqual(response.context['object_list'], ['<Student: Student object>'])
        self.assertContains(response, 'Иван')
        self.assertContains(response, 'Иванов')
        self.assertContains(response, 'Киев, ул. Артема, 6, кв 1')
        self.assertContains(response, 'test')


    def test_students_view_with_3_students(self):
        create_student(name='Иван', surname='Иванов', course=['Python'])
        create_student(name='Петр', surname='Петров', course='Java')
        create_student(name='Сергей', surname='Сидоров', course='php')
        response = self.client.get(reverse('students:list_view'))
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Student: Student object>', '<Student: Student object>'],
                                 ordered=False)
        self.assertEqual(len(response.context['object_list']), 2)

    def test_students_view_with_get_course_id(self):
        create_student(name='Иван', surname='Иванов', course=['Python'])
        create_student(name='Петр', surname='Петров', course=['Java'])
        create_student(name='Сергей', surname='Сидоров', course=['php'])
        client = Client()
        response = client.get('/students/', {'course_id': 3})
        self.assertQuerysetEqual(response.context['object_list'], [])



class StudentsDetailTest(TestCase):
    def test_student_detail(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student = create_student(name='Иван', surname='Иванов', course='Python')
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_student_detail_address(self):
        student = create_student(name='Иван', surname='Иванов', course='Python')
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Киев, ул. Артема, 6, кв 1')

    def test_student_detail_email(self):
        student = create_student(name='Иван', surname='Иванов', course='Python')
        response = self.client.get('/students/1/')
        self.assertContains(response, 'test@gmail.com')

    def test_student_detail_phone(self):
        student = create_student(name='Иван', surname='Иванов', course='Python')
        response = self.client.get('/students/1/')
        self.assertContains(response, '044111111')

    def test_student_in_course(self):
        student = create_student(name='Иван', surname='Иванов', course='Python')
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Иванов Иван')