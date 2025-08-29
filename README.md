# BajajFinservFullStackADRINE22BCE0757
# BFHL API – Flask Project

This project is a REST API built with Flask to handle a POST request at the `/bfhl` route.

### Features

- Accepts an array of mixed data types via POST request
- Returns:
  - Status
  - User ID in `full_name_ddmmyyyy` format
  - Email
  - College Roll Number
  - Even numbers
  - Odd numbers
  - Alphabets in uppercase
  - Special characters
  - Sum of numbers (as string)
  - Reversed concatenation of alphabets in alternating caps

---

### 1. Entire Output Working in Postman

- The API is fully functional and tested using **Postman**.
- Correct output is being returned in the required format.

Screenshot of Postman output is included in the repository.

---

### 2. Heroku CLI Installation Issue

- I tried downloading and installing **Heroku CLI**, but it was not connecting or recognizing commands.
- Due to this, the deployment to Heroku could not be completed.

Screenshot of Heroku CLI issue is also attached in the repository.

---

### Project Files

- `app.py`: Main Flask app
- `requirements.txt`: Python dependencies
- `Procfile`: Tells Heroku how to run the app
- `README.md`: This file

---

### How to Run Locally

```bash
pip install -r requirements.txt
python app.py
