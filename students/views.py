from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from students.models import Student
from .forms import StudentModelForm
#список всех студентвои и одного курса
def list_view(request):
    course_id = request.GET.get('course_id',None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

#данные студента одного
def detail(request,student_id):
    student = get_object_or_404(Student,pk=student_id)
    return render(request,'students/detail.html',{'student':student})

#создание студента
def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print(instance)
            messages.success(request, "Student " + instance.name + " " + instance.surname + " has been successfully added.")
            return redirect('/students/')
    else:
        form = StudentModelForm()
    return render(request,'students/add.html',{'form':form})

#Редактирования студента
def edit(request,student_id):
    student = get_object_or_404(Student,pk=student_id)
    if request.method=="POST":
        form = StudentModelForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Info on the student has been successfully changed.")
            return redirect('/students/edit/'+student_id)
    else:
        form = StudentModelForm(instance=student)
    return render(request,'students/edit.html',{'form':form})

def remove(request,student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method=="POST":
        student.delete()
        messages.success(request, "Info on " + student.name + " " + student.surname + " has been successfully deleted.")
        return redirect('/students/')
    return render(request,'students/remove.html',{'student':student})