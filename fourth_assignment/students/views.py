from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student
from .forms import  StudentForm


# Create your views here.
def student_list(request):
    q = request.GET.get('q', '').strip()
    qs = Student.objects.all()
    if q:
        qs = qs.filter(full_name__icontains=q)
    paginator = Paginator(qs, 10) # 10 per page
    page = request.GET.get('page')
    students = paginator.get_page(page)
    return render(request, 'students/student_list.html', {'students': students, "q": q})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student successfully created')
            return redirect('students:list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, "title": "Add Student"})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student successfully updated')
            return redirect('students:list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, "title": "Edit Student"})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student successfully deleted')
        return redirect('students:list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_confirm_delete.html', {"student": student})