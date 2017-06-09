from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from students.models import Student
from students.forms import StudentModelForm


def list_view(request): 

    course_id = request.GET.get('course_id', '')
    
    if course_id == '':
        student_list = Student.objects.all()
    else:
        student_list = Student.objects.filter(courses=course_id)

    return render(request, "students/list.html", {"student_list": student_list })


def detail(request, student_id): 

    student_obj = Student.objects.get(id=student_id)
    courses_list = student_obj.courses.all()

    return render(request, "students/detail.html", {"student": student_obj, "courses_list": courses_list })


def create(request):

    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Student %s %s has been successfully added." % (instance.name, instance.surname))
            return redirect('students:list_view')

    else:
         form = StudentModelForm()

    return render(request, "students/add.html", {'form': form })


def edit(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect('students:edit', student_id = student.id)
    else:
        form = StudentModelForm(instance=student)

    return render(request, "students/edit.html", {'form': form })


def remove(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Info on %s %s has been successfully deleted." % (student.name, student.surname))
        return redirect('students:list_view')

    return render(request, "students/remove.html", {'student': student })



