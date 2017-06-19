from django.test import TestCase
from django.core.urlresolvers import reverse
from datetime import datetime


from students.models import Student
from courses.models import Course


class StudentsListTest(TestCase):
    def test_page_no_students_status_code(self):
        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200)
    
    def test_page_students_status_code(self):
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test', surname = 'Testov')
        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200)

    def test_students_create(self):
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test', surname = 'Testov')
        self.assertEqual(Student.objects.all().count(), 1)

    def test_students_context(self):
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test', surname = 'Testov')
        response = self.client.get(reverse('students:list_view'))
        self.assertTrue('student_list' in response.context)

    def test_students_items_fields(self):
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test', surname = 'Testov')
        response = self.client.get(reverse('students:list_view'))
        self.assertTrue(student1.surname, 'Testov')

  
   

class StudentsDetailTest(TestCase):
    
    def test_page_students_detail_status_code(self):
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test', surname = 'Testov')
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_students_detail_items(self):
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test', surname = 'Testov')
        response = self.client.get('/students/2/')
        self.assertEqual(response.status_code, 404)

   
    def test_students_detail__url(self):        
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test', surname = 'Testov')
        response = self.client.get(reverse('students:detail', args=(student1.id,)))
        self.assertContains(response, student1.name,  status_code=200)

    def test_students_detail_1(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        course2 = Course.objects.create(name = 'Python for DataScience',
                                        short_description = 'short_description')
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test',
                                          surname = 'Testov')
        student1.courses.add(Course.objects.get(id = 1))
        student1.courses.add(Course.objects.get(id = 2))
        response = self.client.get('/students/1/')
        self.assertEqual(student1.courses.all().count(), 2)
        

    def test_students_detail_2(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        course2 = Course.objects.create(name = 'Python for DataScience',
                                        short_description = 'short_description')
        student1 = Student.objects.create(date_of_birth = datetime(2001, 6, 15),
                                          name = 'Test',
                                          surname = 'Testov')
        student1.courses.add(Course.objects.get(id = 1))
        student1.courses.add(Course.objects.get(id = 2))
        courses_1 = student1.courses.all()
        response = self.client.get('/students/1/')
        self.assertEqual(courses_1[1].name, 'Python for DataScience')

     

# Create your tests here.
