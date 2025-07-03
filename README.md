# 📝 BhaukoBuddy – Django Chat App

Welcome to BhaukoBuddy – a simple yet powerful Django-based chat blog platform.

---

## 🚀 Getting Started – Run the Project Locally

Follow these steps to set up and run the project on your local machine:

### Fork and Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Create virtual environment
python -m venv venv

# Activate it
# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate


pip install -r requirements.txt

pip install django

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

