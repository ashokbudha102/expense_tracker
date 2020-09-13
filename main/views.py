from django.shortcuts import render
from .tables import expenseTable
from .models import Expense
from django.urls import reverse
import datetime
from django.contrib import messages
from .forms import downloadForm
from django.shortcuts import redirect
from django_tables2.export.export import TableExport
# from .filters import FilteredView 
from django_tables2.config import RequestConfig
from django.views.generic import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
@login_required
def home_view(request):
    current_user=request.user
    form=downloadForm()
    table=expenseTable(Expense.objects.filter(addedBy=current_user))
    RequestConfig(request, paginate={"per_page": 8}).configure(table)
    return render(request, 'main/home.html',{'table':table,'user':current_user,'datetime':datetime.datetime.today,'form':form})

class homeCreateView(CreateView, LoginRequiredMixin):
    model=Expense
    success_url = "/"
    fields=['description','amount','date','category']
    def form_valid(self, form):
        form.instance.addedBy=self.request.user
        form.save()
        return super().form_valid(form)
    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.addedBy:
            return True
        return False
    def get_absolute_url(self):
        return redirect()

class expenseDeleteView(LoginRequiredMixin, DeleteView):
    model=Expense
    success_url='/'

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
            

