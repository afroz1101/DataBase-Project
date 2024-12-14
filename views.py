from django.shortcuts import render, redirect, get_object_or_404
from .models import TaxPayments
from django.http import JsonResponse
def tax_payment_form(request):
    success_message = 'None'
    if request.method == 'POST':
        # Get data from the form
        company = request.POST.get('company', '').strip()
        amount = request.POST.get('amount', '').strip()
        payment_date = request.POST.get('payment_date', '').strip()
        status = request.POST.get('status', '').strip()
        due_date = request.POST.get('due_date', '').strip()
        tax_rate = request.POST.get('tax_rate', '').strip()

        # Validation for required fields
        if not company or not amount or not status or not due_date or not tax_rate:
            success_message = "All fields except Payment Date are required."
        else:
            # If payment_date is empty, set it to None
            payment_date = payment_date if payment_date else 'NA'

            # Save data to the database
            TaxPayments.objects.create(
                company=company,
                amount=amount,
                payment_date=payment_date,
                status=status,
                due_date=due_date,
                tax_rate=tax_rate,
            )
            records = TaxPayments.objects.all()
            due_dates = TaxPayments.objects.values('due_date').distinct()
            success_message = "The tax payment has been saved successfully!"
            return render(request, 'index.html', {
                'success_message': success_message,
                'records': records,
                'due_dates': due_dates
            })
    # Fetch all records from the database to display in the table
    records = TaxPayments.objects.all()
    due_dates = TaxPayments.objects.values('due_date').distinct()
    return render(request, 'index.html', {
        'records': records,
        'due_dates': due_dates
    })

def delete_tax_payment(request, record_id):
    tax_payment = get_object_or_404(TaxPayments, id=record_id)
    tax_payment.delete()
    return redirect('home')

def update_tax_payment(request):
    if request.method == 'POST':
        tax_payment_id = request.POST.get('id')
        company = request.POST.get('company')
        amount = request.POST.get('amount')
        payment_date = request.POST.get('payment_date')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        tax_rate = request.POST.get('tax_rate')

        # Get the object to update
        tax_payment = get_object_or_404(TaxPayments, id=tax_payment_id)

        # Update the fields
        tax_payment.company = company
        tax_payment.amount = amount
        tax_payment.payment_date = payment_date
        tax_payment.status = status
        tax_payment.due_date = due_date
        tax_payment.tax_rate = tax_rate
        tax_payment.save()

        return redirect('home')
    return render(request, 'index.html')


def get_records_by_due_date(request):
    due_date = request.GET.get('due_date')  # Get the due_date parameter from the URL

    if not due_date:
        return JsonResponse({"error": "Due date is required"}, status=400)

    # Fetch records that match the due_date
    records = TaxPayments.objects.filter(due_date=due_date)

    # If no records found, return a message
    if not records.exists():
        return JsonResponse({"message": "No records found for the selected due date."}, status=404)

    # Return the records as JSON
    data = {
        "records": list(records.values("id", "company", "amount", "payment_date", "status", "due_date", "tax_rate")),
    }
    return JsonResponse(data)