# DataBase-Project
Tax Payment Tracking System
Overview
The Tax Payment Tracking System is a Django-based web application that helps organizations manage and track tax payments. It allows users to add, update, delete, and filter tax payment records based on due dates. The system also provides a user-friendly interface to monitor the status of payments.
Features
- Add new tax payment records.
- Update existing tax payment records.
- Delete tax payment records.
- Filter and view tax records by due date.
- Maintain distinct due dates for easy reference.
Installation
Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- Django 3.0+
- A database (SQLite is used by default)
Steps
1. Clone the Repository
```bash
git clone https://github.com/your-username/tax-payment-tracking-system.git
cd tax-payment-tracking-system
```
2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Run the Development Server
```bash
python manage.py runserver
```
6. Access the Application
Open your browser and navigate to:
http://127.0.0.1:8000/
Project Structure
```
Tax_Payment_Tracking_System/
|-- manage.py
|-- db.sqlite3
|-- users/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|-- templates/
|   |-- index.html
|-- Tax_Payement_Tracking_System/
    |-- __init__.py
    |-- asgi.py
    |-- settings.py
    |-- urls.py
    |-- wsgi.py
```
Usage
### Adding a Tax Payment
1. Open the application.
2. Fill in the required fields in the form:
   - Company Name
   - Amount
   - Due Date
   - Status
   - Tax Rate
   - (Optional) Payment Date
3. Click the Submit button to save the record.

### Updating a Tax Payment
1. Navigate to the record in the list.
2. Click the Edit button.
3. Modify the fields and save the changes.

### Deleting a Tax Payment
1. Navigate to the record in the list.
2. Click the Delete button to remove the record.

### Filtering by Due Date
1. Select a due date from the dropdown filter.
2. View the filtered list of tax payment records.
API Endpoints
| Endpoint                                    | Description                                        |
| ------------------------------------------- | -------------------------------------------------- |
| `/`                                         | Displays the tax payment form and list of records. |
| `/delete/<int:record_id>/`                  | Deletes a specific tax payment record.             |
| `/update_tax_payment/`                      | Updates an existing tax payment record.            |
| `/get_records_by_due_date/?due_date=<date>` | Fetches records matching a specific due date.      |
Models
The `TaxPayments` model has the following fields:
- **company**: Name of the company.
- **amount**: Amount of the tax payment.
- **payment_date**: Date of the payment (optional).
- **status**: Status of the payment (e.g., Paid, Pending).
- **due_date**: Date when the payment is due.
- **tax_rate**: Tax rate applicable.
Templates
- `index.html`: Main page displaying the form and list of tax payments.
Issues and Contributions
- If you encounter any issues, feel free to open an issue in the GitHub repository.
- Contributions are welcome! Fork the repository, make your changes, and submit a pull request.
  
Author
Afroz Mohd
