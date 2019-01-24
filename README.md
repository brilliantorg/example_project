# example_project

This assumes you have python3 and virtualenv.

```
git clone https://github.com/brilliantorg/example_project.git
cd example_project
mkvirtualenv -p /usr/bin/python3 example_project
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

Then access `http://localhost:8000/example/hello-world/` from your browser.
