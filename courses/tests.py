from django.test import TestCase
from courses.models import Course
from django.test import Client


class CoursesDetailTest(TestCase):
    
    def test_page_no_course(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_pages_1_course(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course_test = Course.objects.create(name='name_course',
                                            short_description='short_descript_course',
                                            description='descript_course')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name_course')    
    
    def test_object_create(self):
        client = Client()
        course_test = Course.objects.create(name='name_course',
                                            short_description='short_descript_course',
                                            description='descript_course')
        response = client.get('/courses/1/')
        self.assertContains(response, 'name_course')
    
    def test_object_change(self):
        client = Client()
        course_test = Course.objects.create(name='name_course',
                                            short_description='short_descript_course',
                                            description='descript_course')
        course_test.name = 'changed_name'
        course_test.save()
        response = client.get('/courses/1/')
        self.assertContains(response, 'changed_name')
    
    def test_object_delete(self):
        client = Client()
        course_test = Course.objects.create(name='name_course',
                                            short_description='short_descript_course',
                                            description='descript_course')
        course_test.delete()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        
class CoursesListTest(TestCase):
    
    def test_page_no_course(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_pages_1_course(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        course_test = Course.objects.create(name='name_course',
                                            short_description='short_descript_course',
                                            description='descript_course')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, 'name_course')
    
    def test_object_create(self):
        client = Client()
        course_test = Course.objects.create(name='name_course',
                                            short_description='short_descript_course',
                                            description='descript_course')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, 'name_course')
    
    def test_object_change(self):
        client = Client()
        course_test = Course.objects.create(name='name_course',
                                            short_description='short_descript_course',
                                            description='descript_course')
        course_test.name = 'changed_name'
        course_test.save()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, 'changed_name')
    
    def test_object_delete(self):
        client = Client()
        course_test = Course.objects.create(name='name_course',
                                            short_description='short_descript_course',
                                            description='descript_course')
        course_test.delete()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
