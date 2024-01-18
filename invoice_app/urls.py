from django.urls import path
from . import views

urlpatterns = [
    path('invoices/',views.InvoiceCreateListView.as_view()),
    path('invoices/<int:pk>/',views.InvoiceUpdateDeleteRetrive.as_view()),
    path('invoicesDetail/',views.InvoiceDetailCreateListView.as_view()),
    path('invoicesDetail/<int:pk>/',views.InvoiceDetailUpdateDeleteRetrive.as_view()),
]
