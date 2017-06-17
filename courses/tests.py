from django.test import TestCase
from courses.models import Course, Lesson

class CoursesListTest(TestCase):
    
    def test_courses_create(self):
        create_course('Test')
        self.assertEqual(Course.objects.all().count(), 1)
    
    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        create_course('Test')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        
    def test_course_title(self):
        from django.test import Client
        client = Client()
        create_course('Test')
        response = client.get('/courses/1/')
        self.assertContains(response, 'Test')
    
    def test_course_count(self):
        from django.test import Client
        client = Client()
        create_course('Test')
        create_course('Test2')
        create_course('Test3')
        response = client.get('/courses/3/')
        self.assertEqual(response.status_code, 200)
    
    def test_course_del_update(self):
        from django.test import Client
        client = Client()
        create_course('Test')
        create_course('Test2')
        create_course('Test3')
        response = client.get('/')
        self.assertContains(response, '<a href="/courses/add/" class="btn btn-primary">Add new course</a>')
        self.assertContains(response, '<a href="/courses/remove/1/" class="btn btn-danger">Remove course</a>')
        


        
def create_course(name):
    course = Course.objects.create(name=name, short_description = 'short_description', description='description')
    return course
    
def create_lesson(subject, name):
    lesson = Lesson.objects.create(subject=subject, course=name, description='description', order=1)
    return lesson
    
    
class CoursesDetailTest(TestCase):
    
    def test_courses_create(self):
        create_course('Test')
        self.assertEqual(Course.objects.all().count(), 1)
    
    def test_pages(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        create_course('Test')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_course_new_lesson(self):
        from django.test import Client
        client = Client()
        create_course('Test')
        response = client.get('/courses/1/')
        self.assertContains(response, '<a href="/courses/1/add_lesson" class="btn btn-primary">Add new lesson</a>')
        
    def test_course_add_lesson(self):
        from django.test import Client
        client = Client()
        course = create_course('Test')
        create_lesson('Lesson1', course)
        response = client.get('/courses/1/')
        self.assertContains(response, 'Lesson1')
        
    def test_course_add_diff_lesson(self):
        from django.test import Client
        client = Client()
        course1 = create_course('Test')
        course2 = create_course('Test2')
        create_lesson('Lesson1', course1)
        create_lesson('Lesson2', course2)
        response = client.get('/courses/1/')
        self.assertNotContains(response, 'Lesson2')
            

# Create your tests here.
