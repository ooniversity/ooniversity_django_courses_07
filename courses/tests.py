from django.test import TestCase
from django.test import Client
from .models import Course

# Create your tests here.
class CoursesListTest(TestCase):
    
    def test_list_status(self):
        client = Client()
        
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_content(self):
        client = Client()
        
        response = client.get('/')
        self.assertContains(response, 'rymka1989')
        
        
    def test_template(self):
        client = Client()
        
        response = client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        
        
    def test_list_add_link(self):
        client = Client()
        
        response = client.get('/')
        self.assertContains(response, '/courses/add/')
        
    def test_list_text(self):
        client = Client()
        
        response = client.get('/')
        self.assertContains(response, 'Bursa')
        
        
        
class CoursesDetailTest(TestCase):
    
    def test_create(self):
        Course.objects.create(name='1', short_description='--', description='==')
        
        self.assertEqual(Course.objects.all().count(), 1)

    
    def test_status(self):
        Course.objects.create(name='1', short_description='--', description='==')
        client = Client()
         
        response = client.get('/courses/detail/1/')
        self.assertEqual(response.status_code, 200)
        
    
    def test_content(self):
        Course.objects.create(name='Python', short_description='--', description='==')
        client = Client()
         
        response = client.get('/courses/detail/1/')
        self.assertContains(response, 'Python')
         
         
    def test_content_1(self):
        Course.objects.create(name='Python', short_description='--', description='==')
        client = Client()
         
        response = client.get('/courses/detail/1/')
        self.assertNotContains(response, 'Django')
         
         
    def test_template(self):
        Course.objects.create(name='Python', short_description='--', description='==')
        client = Client()
         
        response = client.get('/courses/detail/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')