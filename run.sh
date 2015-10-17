rm dist/redwine*
python setup.py sdist
cd ../online
pip uninstall redwine -y
pip install ../redwine/dist/redwine-1.2.2.tar.gz
python manage.py runserver 0.0.0.0:8080

