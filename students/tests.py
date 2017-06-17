from django.test import TestCase
from students.models import Student
from courses.models import Course

class StudentsListTest(TestCase):
    
    def test_student_create(self):
        create_student('Test')
        self.assertEqual(Student.objects.all().count(), 1)
 
    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        create_student('Test')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        
    def test_students_count(self):
        from django.test import Client
        client = Client()
        create_student('Test')
        create_student('Test1')
        create_student('Test2')
        response = client.get('/students/3/')
        self.assertEqual(response.status_code, 200)
    
    def test_students_del_update(self):
        from django.test import Client
        client = Client()
        create_student('Test2')
        response = client.get('/students/')
        self.assertContains(response, '<a href="/students/edit/1/" class="btn btn-info">Изменить</a>')
        
    def test_students_add(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/add/')
        self.assertEqual(response.status_code, 200)


        
def create_student(name):
    student = Student.objects.create(name=name, surname='surname', date_of_birth='1988-12-12', email='asd@as.ss',
                                    phone='2324', address='sdfs', skype=name)
    return student



class StudentsDetailTest(TestCase):
    
    def test_student_create(self):
        create_student('Test')
        self.assertEqual(Student.objects.all().count(), 1)
    
    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        create_student('Test')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_student_title(self):
        from django.test import Client
        client = Client()
        create_student('Test_title')
        response = client.get('/students/1/')
        self.assertContains(response, 'Test_title')
        
    def test_skype(self):
        from django.test import Client
        client = Client()
        create_student('TESTTT')
        response = client.get('/students/1/')
        self.assertContains(response, '<td>TESTTT</td>')
        
    def test_student_add_diff_stud(self):
        from django.test import Client
        client = Client()
        create_student('Test')
        create_student('Test2')
        response = client.get('/students/2/')
        self.assertContains(response, 'Test2')
# Create your tests here.
