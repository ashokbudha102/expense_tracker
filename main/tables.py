import django_tables2 as tables
from .models import Expense
from django_tables2.utils import A
class expenseTable(tables.Table):
    delete = tables.LinkColumn('delete',text='delete',args=[A('pk')])
    class Meta:
        model=Expense
        exclude=('addedBy',)
        order_by='-id'
        template_name='django_tables2/bootstrap4.html'




