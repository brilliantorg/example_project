# example_project

This assumes you have python3 and virtualenv.

```
git clone https://github.com/brilliantorg/example_project.git
cd example_project
mkvirtualenv -p `which python3` example_project
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

Then access `http://localhost:8000/example/hello-world/` from your browser.

This example uses the `mkvirtualenv` command from `virtualenvwrapper`. This can be prepared on a
modern ubuntu by `sudo apt-get install virtualenvwrapper`, and then adding the following to your
`.bashrc`.

```
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
```
