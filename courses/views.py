from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, course_id):
    course_inf = Course.objects.get(id=course_id)
    teacher = {'f_name': course_inf.coach.user.first_name, 
                'l_name': course_inf.coach.user.last_name,
                'descr': course_inf.coach.description,
                'id': course_inf.coach.id}
    assistant = {'f_name': course_inf.assistant.user.first_name, 
                'l_name': course_inf.assistant.user.last_name,
                'descr': course_inf.assistant.description,
                'id': course_inf.assistant.id}
    print(assistant)
    course_plan = Lesson.objects.filter(course=course_id)
    return render(request, 'courses/detail.html', {'course_inf': course_inf, 'course_plan': course_plan,
                                                    'teacher': teacher, 'assistant': assistant})


# Create your views here.
