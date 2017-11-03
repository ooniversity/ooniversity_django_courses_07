from django.test import TestCase
from django.test import Client
from .models import Student

# Create your tests here.
class StudentsListTest(TestCase):
    
    def test_list_status(self):
        client = Client()
        
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        
    def test_list_status_1(self):
        client = Client()
        
        response = client.get('/students/?course_id=1')
        self.assertEqual(response.status_code, 200)
        
    def test_list_status_2(self):
        client = Client()
        
        response = client.get('/students/?page=100')
        self.assertEqual(response.status_code, 404)
        
        
    def test_content(self):
        client = Client()
        
        response = client.get('/students/')
        self.assertContains(response, 'rymka1989')
        
        
    def test_template(self):
        client = Client()
        
        response = client.get('/students/?page=1')
        self.assertTemplateUsed(response, 'students/student_list.html')
        
        
    def test_list_add_link(self):
        client = Client()
        
        response = client.get('/students/')
        self.assertContains(response, '/students/add/')
        
        
        
class StudentsDetailTest(TestCase):
    
    def test_create(self):
        Student.objects.create(
                                name='1',
                                surname='2',
                                date_of_birth='1989-06-17',
                                email='123@123.com',
                                phone='000',
                                address='---',
                                skype='---'
                            )
        
        self.assertEqual(Student.objects.all().count(), 1)

    
    def test_status(self):
        Student.objects.create(
                                name='1',
                                surname='2',
                                date_of_birth='1989-06-17',
                                email='123@123.com',
                                phone='000',
                                address='---',
                                skype='---'
                            )
        client = Client()
          
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
         
     
    def test_content(self):
        Student.objects.create(
                                name='1',
                                surname='2',
                                date_of_birth='1989-06-17',
                                email='123@123.com',
                                phone='000',
                                address='---',
                                skype='---'
                            )
        client = Client()
           
        response = client.get('/students/1/')
        self.assertContains(response, '---')
          
          
    def test_content_1(self):
        Student.objects.create(
                                name='1',
                                surname='2',
                                date_of_birth='1989-06-17',
                                email='123@123.com',
                                phone='000',
                                address='---',
                                skype='---'
                            )
        client = Client()
           
        response = client.get('/students/1/')
        self.assertNotContains(response, '1234@123.com')
          
          
    def test_template(self):
        Student.objects.create(
                                name='1',
                                surname='2',
                                date_of_birth='1989-06-17',
                                email='123@123.com',
                                phone='000',
                                address='---',
                                skype='---'
                            )
        client = Client()
          
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')