from django.shortcuts import render
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

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

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            course = form.cleaned_data['name']
            messages.success(request, ('Course %s has been successfully added.' % course))
            return redirect('index')
    else:
        form = CourseModelForm()
    context = {'form': form}
    return render(request, 'courses/add.html', context)


def edit(request, id):
    course = Course.objects.get(id=id)
    form = CourseModelForm(instance=course)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, ('The changes have been saved.'))
            return redirect('courses:edit', id=id)
    context = {'form': form}
    return render(request, 'courses/edit.html', context)


def remove(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, ('Course %s has been deleted.' % course.name))
        return redirect('index')
    context = {'course': course}
    return render(request, 'courses/remove.html', context)
    
def add_lesson(request, id):
    course = Course.objects.get(id=id)
    form = LessonModelForm(initial={'course': course})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, ('Lesson %s has been successfully added.' % lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    context = {'form': form, 'course': course}
    return render(request, 'courses/add_lesson.html', context)
# Create your views here.
