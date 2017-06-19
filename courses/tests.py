from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Course, Lesson


class CoursesListTest(TestCase):
    def test_page_no_courses_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_page_courses_status_code(self):
        course1 = Course.objects.create(name = 'Python',
                                       short_description = 'short_description')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        self.assertEqual(Course.objects.all().count(), 1)

    def test_courses_context(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        response = self.client.get(reverse('index'))
        self.assertTrue('courses' in response.context)

    def test_courses_items_fields(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        response = self.client.get(reverse('index'))
        self.assertTrue(course1.short_description, 'short_description')

  
   

class CoursesDetailTest(TestCase):
    
    def test_page_courses_detail_status_code(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_detail_items(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        response = self.client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_course_detail__url(self):        
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        course2 = Course.objects.create(name = 'Python for DataScience',
                                        short_description = 'short_description')
        response = self.client.get(reverse('courses:detail', args=(course2.id,)))
        self.assertContains(response, course2.name,  status_code=200)

    def test_course_detail_1(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        lesson1 = Lesson.objects.create(course=course1,
                                        subject='Intro to Python',
                                        order=1)
        lesson2 = Lesson.objects.create(course=course1,
                                        subject='STDLib',
                                        order=2)
        lessons = course1.lesson_set.all()
        response = self.client.get('/courses/1/')
        self.assertEqual(course1.lesson_set.all().count(), 2)
        

    def test_course_detail_2(self):
        course1 = Course.objects.create(name = 'Python',
                                        short_description = 'short_description')
        lesson1 = Lesson.objects.create(course=course1,
                                        subject='Intro to Python',
                                        order=1)
        lesson2 = Lesson.objects.create(course=course1,
                                        subject='STDLib',
                                        order=2)
        lessons = course1.lesson_set.all()
        response = self.client.get('/courses/1/')
        self.assertEqual(lessons[0].subject, 'Intro to Python')
        self.assertEqual(lessons[1].order, 2)

# Create your tests here.
