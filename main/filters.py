# from django_filters.views import FilterView
# from django_tables2.views import SingleTableMixin
# from .tables import expenseTable
# from .models import Expense
# class FilteredView(SingleTableMixin, FilterView):
#     table_class=expenseTable
#     model=Expense
#     template_name='main/base.html'

import django_filters
from .models import Expense
class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model=Expense
        fields=['description','amount','date','category']