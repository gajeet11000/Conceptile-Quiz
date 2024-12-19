# Conceptile-Quiz

A Django app for taking quizes. The quiz questions needs to be preloaded from the `quizes.csv` file.

To get it running yourself:

1. Clone the repository using `git clone https://github.com/gajeet11000/Conceptile-Quiz.git`
2. Change into the directory `cd Conceptile-Quiz`
3. Create a virtual environment `python -m venv venv` (on Windows) or `python3 -m venv venv` (on macOS/Linux)
4. Activate the virtual environment `venv\Scripts\activate` (on Windows) or `source venv/bin/activate` (on macOS/Linux)
5. Install the dependencies `pip install -r requirements.txt`
7. Run the migrations `python manage.py migrate`
8. Import the quiz questions into database `python manage.py load_questions` 
9. Run the server `python manage.py runserver`

> Please don't forget to import the questions using **python manage.py load_questions**