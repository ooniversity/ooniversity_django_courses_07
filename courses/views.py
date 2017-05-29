from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, course_id):
    course_info = Course.objects.get(id=course_id)
    teacher = {'first_name': course_info.coach.user.first_name, 
                'last_name': course_info.coach.user.last_name,
                'description': course_info.coach.description,
                'id': course_info.coach.id}
    assistant = {'first_name': course_info.assistant.user.first_name, 
                'last_name': course_info.assistant.user.last_name,
                'description': course_info.assistant.description,
                'id': course_info.assistant.id}
    
    course_plan = Lesson.objects.filter(course=course_id)
    return render(request, 'courses/detail.html', {'course_info': course_info, 'course_plan': course_plan,
                                                    'teacher': teacher, 'assistant': assistant})


# Create your views here.
