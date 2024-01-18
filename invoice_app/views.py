from django.shortcuts import render
from rest_framework import generics
from .serializers import Invoice, InvoiceDetail, InvoiceSerializer, InvoiceDetailSerializer
# Create your views here.

class InvoiceCreateListView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceUpdateDeleteRetrive(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailCreateListView(generics.ListCreateAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer


class InvoiceDetailUpdateDeleteRetrive(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

