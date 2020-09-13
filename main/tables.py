import django_tables2 as tables
from .models import Expense
class expenseTable(tables.Table):
    class Meta:
        model=Expense
        exclude=('addedBy',)
        template_name='django_tables2/bootstrap4.html'




