from django.test import TestCase
from students.models import Student
from django.test import Client
        
        
class StudentsDetailTest(TestCase):
    
    def test_page_no_student(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

    def test_pages_1_student(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        student_test = Student.objects.create(name='name_student',
                                            surname='surname_student',
                                            date_of_birth='1983-07-07',
                                            phone='91284234',
                                            address='asfklj',
                                            skype='dsfgsf',
                                            email='sada@dfs.com')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name_student')    
    
    def test_object_create(self):
        client = Client()
        student_test = Student.objects.create(name='name_student',
                                            surname='surname_student',
                                            date_of_birth='1983-07-07',
                                            phone='91284234',
                                            address='asfklj',
                                            skype='dsfgsf',
                                            email='sada@dfs.com')
        response = client.get('/students/1/')
        self.assertContains(response, 'name_student')
    
    def test_object_change(self):
        client = Client()
        student_test = Student.objects.create(name='name_student',
                                            surname='surname_student',
                                            date_of_birth='1983-07-07',
                                            phone='91284234',
                                            address='asfklj',
                                            skype='dsfgsf',
                                            email='sada@dfs.com')
        student_test.name = 'changed_name'
        student_test.save()
        response = client.get('/students/1/')
        self.assertContains(response, 'changed_name')
    
    def test_object_delete(self):
        client = Client()
        student_test = Student.objects.create(name='name_student',
                                            surname='surname_student',
                                            date_of_birth='1983-07-07',
                                            phone='91284234',
                                            address='asfklj',
                                            skype='dsfgsf',
                                            email='sada@dfs.com')
        student_test.delete()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

class StudentsListTest (TestCase):
    
    def test_page_no_student(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_pages_1_student(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        student_test = Student.objects.create(name='name_student',
                                            surname='surname_student',
                                            date_of_birth='1983-07-07',
                                            phone='91284234',
                                            address='asfklj',
                                            skype='dsfgsf',
                                            email='sada@dfs.com')
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name_student')    
    
    def test_object_create(self):
        client = Client()
        student_test = Student.objects.create(name='name_student',
                                            surname='surname_student',
                                            date_of_birth='1983-07-07',
                                            phone='91284234',
                                            address='asfklj',
                                            skype='dsfgsf',
                                            email='sada@dfs.com')
        response = client.get('/students/')
        self.assertContains(response, 'name_student')
    
    def test_object_change(self):
        client = Client()
        student_test = Student.objects.create(name='name_student',
                                            surname='surname_student',
                                            date_of_birth='1983-07-07',
                                            phone='91284234',
                                            address='asfklj',
                                            skype='dsfgsf',
                                            email='sada@dfs.com')
        student_test.name = 'changed_name'
        student_test.save()
        response = client.get('/students/')
        self.assertContains(response, 'changed_name')
    
    def test_object_delete(self):
        client = Client()
        student_test = Student.objects.create(name='name_student',
                                            surname='surname_student',
                                            date_of_birth='1983-07-07',
                                            phone='91284234',
                                            address='asfklj',
                                            skype='dsfgsf',
                                            email='sada@dfs.com')
        student_test.delete()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
