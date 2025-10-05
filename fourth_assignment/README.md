### Prerequisites
Python 3.8 or higher
Git
pip (Python package installer)
### Step-by-Step Setup
##### Clone the Repository Open your terminal and run:
``git clone https://github.com/c0ff33py/Assignment.git``

``cd Assignment/fourth_assignment``

#### Create a Virtual Environment (Recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

#### Install requiremets
pip install -r requirements.txt

### Apply migrations
python manage.py makemigrations
python manage.py migrate

### Run the development server
python manage.py runserver

### Android 
- first install termux from app store
- in terminal 'pkg install git'
- ``git clone https://github.com/c0ff33py/Assignment.git``
- cd Assignment/fourth_assignment
- `pkg install python`
- run `python manage.py runserver`
- then copy link 'http://127.0.0.1:8000/' to browser
