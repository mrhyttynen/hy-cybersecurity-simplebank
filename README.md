This project demonstrates 5 vulnerabilities from the 2021 version of the OWASP Top 10 vulnerabilities list (found at https://owasp.org/Top10/2021/), using a simple peer-to-peer banking application. The application was built using Django, following the template established in the exercises of the Securing Software course. To run the app (assuming you have the dependencies used in securing software):

In repository root run 
- `pip install django-cryptography`
- `python3 manage.py migrate`
- `python3 manage.py runserver` and go to http://127.0.0.1:8000/ 

Functionality
- Create a user with any username and email
- Login using default password
- Change the password if you want & login again
- Create another user
- Transfer money between users
- If logs don’t start being written into the insecurebank.log file (the app should log user creation, login and transfer events), delete it and db.sqlite3 and run the above steps again
