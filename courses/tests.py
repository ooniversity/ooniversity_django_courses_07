from django.test import TestCase
from students.models import Course
from django.test import Client

client = Client()

class CoursesListTest(TestCase):
    
    def test_student_exist(self):
        Course.objects.create()
        exist = Course.objects.all().count()
        self.assertEqual(exist,1)
	
    def test_pages(self):
  
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
	
    def test_course_name(self):
  
        Course.objects.create(name = 'Python')
        response = self.client.get('/courses/1/')
        self.assertContains(response,'Python')
	
    def test_course_not_exist1(self):
        exist = Course.objects.all().count()
        self.assertFalse(exist)
	
    def test_course_not_exist2(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        


class CoursesDetailTest(TestCase):
    
    def test_course_detail_exist(self):
        Course.objects.create()
        exist = Course.objects.all().count()
        self.assertEqual(exist,1)
	
    def test_detail_pages(self):
        Course.objects.create()
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
	
    def test_course_detail_name(self):
  
        Course.objects.create(name = 'Python')
        response = self.client.get('/courses/1/')
        self.assertContains(response,'Python')
	
    def test_course_detail_not_exist1(self):
        Course.objects.create()
        response = self.client.get('/courses/edit/1/')
        self.assertEqual(response.status_code, 200)
	
    def test_student_detail_not_exist2(self):
        Course.objects.create()
        response = self.client.get('/courses/remove/1/')
        self.assertEqual(response.status_code, 200)
        
# Create your tests here.
