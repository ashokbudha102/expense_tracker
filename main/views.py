from django.shortcuts import render
from .tables import expenseTable
from .models import Expense,ExpenseCategory
from django.urls import reverse
from django.contrib import messages
import datetime
from django.shortcuts import reverse
from .forms import downloadForm, ExpenseForm
from django.shortcuts import redirect
from django_tables2.export.export import TableExport
from .filters import ExpenseFilter
from django_tables2.config import RequestConfig
from django.contrib.auth.decorators import login_required
@login_required
def home_view(request):
    current_user=request.user
    table = expenseTable(Expense.objects.filter(addedBy=current_user))
    RequestConfig(request, paginate={"per_page": 8}).configure(table)
    expForm=ExpenseForm()
    if request.method=='POST':
        expForm=ExpenseForm(request.POST)
        if expForm.is_valid():
            expForm.instance.addedBy=request.user
            expForm.save()
            expForm=ExpenseForm()
            messages.success(request,'Expense added successfully !!')
            return redirect('home')
    return render(request, 'main/home.html',{'table':table,'user':current_user,'form':expForm})

@login_required
def delete_item(request, pk):
    Expense.objects.filter(id=pk).delete()
    items=Expense.objects.filter(addedBy=request.user)
    context={"items":items}
    messages.success(request,'Item deleted successfully')
    return redirect(reverse('home'))


@login_required
def downloadView(request):
    current_user = request.user
    downForm=downloadForm()
    table = None
    if request.method=='GET':
        downForm = downloadForm(request.GET)
        if downForm.is_valid():
            start=downForm.cleaned_data['startingDate']
            end=downForm.cleaned_data['endingDate']
            table = expenseTable(Expense.objects.filter(date__range=[start,end]))
            messages.success(request, 'Your file is download ready!!!')
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table,
                               exclude_columns=("addedBy"))
        return exporter.response("table.{}".format(export_format))


    return render(request, 'main/down.html',{'form':downForm,'table':table})
            

@login_required
def summary(request):
    current=ExpenseCategory.objects.all()
    return render(request,'main/summary.html',{'current':current})

