# example_project

This assumes you have python3 and virtualenv.

```
git clone https://github.com/brilliantorg/example_project.git
cd example_project
python3 -m venv ~/.virtualenvs/example_project
source ~/.virtualenvs/example_project/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

Then access `http://localhost:8000/example/hello-world/` from your browser.
