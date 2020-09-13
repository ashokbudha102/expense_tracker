from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ExpenseCategory(models.Model):
    categoryName=models.CharField(max_length=100)
    def __str__(self):
        return self.categoryName
class Expense(models.Model):
    description=models.CharField(max_length=100, blank=True, null=True)
    amount=models.DecimalField(max_digits=18, decimal_places=2, default=0)
    date=models.DateField()
    addedBy=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category=models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.date}-{self.category}-{self.amount}'
