# Question 1 - SEN 202 Exam

**Name:** Kelvin Mordi  
**Matric Number:** VUGSEN2412771  
**GitHub Username:Valhallaking456
**Email:** kelvinmor13@gmail.com

## Description
This project contains a Django REST API that models a staff database with:
- A base class: `StaffBase`
- Two derived classes: `Manager` and `Intern`
- Serializers with field hiding
- A browsable API via Django REST Framework

## How to Run
1. Install dependencies:  
   `pip install -r requirements.txt`
2. Run migrations:  
   `python manage.py makemigrations`  
   `python manage.py migrate`
3. Start the server:  
   `python manage.py runserver`
4. Test endpoints:
   - `http://127.0.0.1:8000/api/managers/`
   - `http://127.0.0.1:8000/api/interns/`
