from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Inquiry
from .forms import InquiryForm, ResolveForm

# Create your views here.
def inquiry_list(request):
    inquiries = Inquiry.objects.all()
    return render(request, 'inquiry/inquiry_list.html', {'inquiries': inquiries})

def inquiry_detail(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    return render(request, 'inquiry/inquiry_detail.html', {'inquiry': inquiry})

def inquiry_new(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.date = timezone.now()
            inquiry.save()
            return redirect('inquiry_detail', pk=inquiry.pk)
    else:
        form = InquiryForm()
    return render(request, 'inquiry/inquiry_edit.html', {'form': form})

def inquiry_edit(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    if request.method == "POST":
        form = ResolveForm(request.POST, instance=inquiry)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.date = timezone.now()
            inquiry.save()
            return redirect('inquiry_detail', pk=inquiry.pk)
    else:
        form = ResolveForm(instance=inquiry)
    return render(request, 'inquiry/inquiry_resolve.html', {'form': form})

def inquiry_pending(request):
    inquiries = Inquiry.objects.filter(status='Pending').order_by('date')
    return render(request, 'inquiry/inquiry_pending.html', {'inquiries': inquiries})

def inquiry_resolved(request):
    inquiries = Inquiry.objects.filter(status='RESOLVED').order_by('date')
    return render(request, 'inquiry/inquiry_resolved.html', {'inquiries': inquiries})

def inquiry_task(request):
    inquiries = Inquiry.objects.filter(department='CUSTOMER CARE', status='Pending').order_by('date')
    return render(request, 'inquiry/inquiry_task.html', {'inquiries': inquiries})

