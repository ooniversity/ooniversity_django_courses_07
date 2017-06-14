from django.test import TestCase, Client
from courses.models import Course, Lesson
from students.models import Student
from django.urls import reverse
from datetime import datetime


client = Client()


class StudentsDetailTest(TestCase):

    def create_student(self, course=None, name='Student 1', surname='SecondName', email='test@test.com'):
        student = Student.objects.create(
                        name=name,
                        surname=surname, 
                        date_of_birth=datetime.now(), 
                        email=email, 
                        phone='1234567890', 
                        address='Kharkiv', 
                        skype='Skype', 
                        #courses=Course.objects.get(id=course.id),
                )
        if course:
            student.courses.add(course)
        return student


    def test_student_create(self):
        course_test = CoursesDetailTest()
        course = course_test.create_course()
        student = self.create_student(course, 'Cat', 'Gagarinova', 'cat@mail.com')
        self.assertEqual(Student.objects.all().count(), 1)


    def test_student_detailview(self):
        student = self.create_student()
        response = self.client.get(reverse('students:detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)


    def test_not_existing_student(self):
        response = self.client.get(reverse('students:detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, 404)


    def test_student_detailview_info(self):
        student = self.create_student()
        response = self.client.get(reverse('students:detail', kwargs={'pk': student.id}))
        std = response.context['object']
        self.assertEqual(std.name, 'Student 1')
        self.assertEqual(std.surname, 'SecondName')
        self.assertEqual(std.email, 'test@test.com')


    def test_student_detailview_email_is_unique(self):
        student = self.create_student()
        response = self.client.get(reverse('students:detail', kwargs={'pk': student.id}))
        std = response.context['object']
        emails = Student.objects.filter(email=std.email)
        self.assertEqual(emails.count(), 1)



class StudentsListTest(TestCase):
    
    def test_student_listview_show_empty(self):
        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200)


    def test_student_listview_show_3(self):
        student_test = StudentsDetailTest()
        student_test.create_student(email='mail1@m.ua')
        student_test.create_student(email='mail2@m.ua')
        student_test.create_student(email='mail3@m.ua')
        response = self.client.get(reverse('students:list_view'))
        #print(response.context)
        # paginate_by = 2
        self.assertEqual(response.context['student_list'].count(), 2)


    def test_student_listview_empty_paginated(self):
        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.context['is_paginated'], False)

        
    def test_student_listview_paginated_page_count(self):
        student_test = StudentsDetailTest()
        student_test.create_student(email='mail1@m.ua')
        student_test.create_student(email='mail2@m.ua')
        student_test.create_student(email='mail3@m.ua')
        student_test.create_student(email='mail4@m.ua')
        student_test.create_student(email='mail5@m.ua')
        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.context['page_obj'].paginator.num_pages, 3)


    def test_student_listview_show_students_for_course(self):
        course_test = CoursesDetailTest()
        student_test = StudentsDetailTest()
        course = course_test.create_course()
        student_test.create_student(course=course, email='mail1@m.ua')
        student_test.create_student(email='mail2@m.ua')
        student_test.create_student(email='mail3@m.ua')
        student_test.create_student(course=course, email='mail4@m.ua')
        student_test.create_student(email='mail5@m.ua')
        response = self.client.get('/students/?course_id=%s' % course.id)
        self.assertEqual(response.context['is_paginated'], False)


class CoursesDetailTest(TestCase):

    def create_course(self, name='Test Course', short_description='Test Short Description'):
        course = Course.objects.create(
                        name=name,
                        short_description=short_description, )
        return course


    def create_lesson(self, course, subject='Test Lesson', description='Lesson Description'):
        lesson = Lesson.objects.create(
                        subject=subject,
                        description=description,
                        course=Course.objects.get(id=course.id),
                        order=1, )
        return lesson


    def test_course_create(self):
        course = self.create_course('Test Course 1', 'Description test course 1')
        self.assertEqual(Course.objects.all().count(), 1)
        course = self.create_course('Test Course 2', 'Description test course 2')
        self.assertEqual(Course.objects.all().count(), 2)
        course = self.create_course('Test Course 3', 'Description test course 3')
        self.assertEqual(Course.objects.all().count(), 3)


    def test_lesson_create(self):
        course = self.create_course()
        self.assertEqual(Course.objects.all().count(), 1)
        lesson = self.create_lesson(course, 'Test Lesson 1', 'Description test lesson 1')
        self.assertEqual(Lesson.objects.all().count(), 1)
        lesson = self.create_lesson(course, 'Test Lesson 2', 'Description test lesson 2')
        self.assertEqual(Lesson.objects.all().count(), 2)
        lesson = self.create_lesson(course, 'Test Lesson 3', 'Description test lesson 3')
        self.assertEqual(Lesson.objects.all().count(), 3)

        lessons = Lesson.objects.filter(course=course.id)
        self.assertEqual(lessons.count(), 3)


    def test_course_detailview(self):
        course = self.create_course()
        response = self.client.get(reverse('courses:detail', kwargs={'pk': 1}))
        #print(response)
        #print(response.context)
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "No polls are available.")
        #self.assertQuerysetEqual(response.context['latest_question_list'], [])


    def test_not_existing_course(self):
        response = self.client.get(reverse('courses:detail', kwargs={'pk': 10}))
        #print(response)
        #print(response.context)
        #print(response.context['request'])
        self.assertEqual(response.status_code, 404)

    def test_course_name(self):
        course = self.create_course()
        response = self.client.get(reverse('courses:detail', kwargs={'pk': course.id}))
        self.assertContains(response, "Test Course")



class CoursesListTest(TestCase):

    
    def test_course_create(self):
        course_test = CoursesDetailTest()
        course_test.create_course('Test Course 1', 'Description test course 1')
        self.assertEqual(Course.objects.all().count(), 1)


    def test_course_listview_show_empty(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


    def test_course_listview_show_3(self):
        course_test = CoursesDetailTest()
        course_test.create_course()
        course_test.create_course()
        course_test.create_course()
        response = self.client.get(reverse('index'))
        #print(response.context)
        self.assertEqual(response.context['courses_list'].count(), 3)


    def test_course_listview_create_detailview_back_delete(self):
        course_test = CoursesDetailTest()
        course = course_test.create_course()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('courses:detail', kwargs={'pk': course.id}))
        self.assertEqual(response.status_code, 200)
        course.delete()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['courses_list'].count(), 0)
        

    def test_course_listview_create_goto_students(self):
        course_test = CoursesDetailTest()
        course = course_test.create_course()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('students:list_view'))
        #print(response.context)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['student_list'].count(), 0)

