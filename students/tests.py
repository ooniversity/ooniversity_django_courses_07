from django.test import TestCase
from students.models import Student
from django.test import Client

client = Client()

class StudentsListTest(TestCase):
    
    def test_student_exist(self):
        Student.objects.create(date_of_birth = '2013-01-01')
        exist = Student.objects.all().count()
        self.assertEqual(exist,1)
	
    def test_pages(self):
  
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
	
    def test_student_name(self):
  
        student = Student.objects.create(name = 'Ivan', date_of_birth = '2013-01-01')
        response = self.client.get('/students/1/')
        self.assertContains(response,'Ivan')
	
    def test_student_not_exist1(self):
        exist = Student.objects.all().count()
        self.assertFalse(exist)
	
    def test_student_not_exist2(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        


class StudentsDetailTest(TestCase):
    
    def test_student_detail_exist(self):
        Student.objects.create(date_of_birth = '2013-01-01')
        exist = Student.objects.all().count()
        self.assertEqual(exist,1)
	
    def test_detail_pages(self):
        Student.objects.create(date_of_birth = '2013-01-01')
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
	
    def test_student_detail_name(self):
  
        student = Student.objects.create(name = 'Boris', date_of_birth = '2013-01-01')
        response = self.client.get('/students/1/')
        self.assertContains(response,'Boris')
	
    def test_student_detail_not_exist1(self):
        student = Student.objects.create(name = 'Boris', date_of_birth = '2013-01-01')
        response = self.client.get('/students/edit/1/')
        self.assertEqual(response.status_code, 200)
	
    def test_student_detail_not_exist2(self):
        student = Student.objects.create(name = 'Boris', date_of_birth = '2013-01-01')
        response = self.client.get('/students/remove/1/')
        self.assertEqual(response.status_code, 200)
        
# Create your tests here.
