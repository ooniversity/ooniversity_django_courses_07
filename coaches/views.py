from django.shortcuts import render
from coaches.models import Coach


def detail(request, coach_id):
    context = {
        'coach': Coach.objects.get(id=coach_id),
        # 'lessons_list': Lesson.objects.filter(course_id=course_id),
    }

    return render(request, 'coaches/detail.html', context)
