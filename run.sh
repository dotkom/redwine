rm dist/redwine*
python setup.py sdist
cd ../online
source ../env_online/bin/activate
pip uninstall redwine -y
pip install ../redwine/dist/redwine-*.tar.gz
python manage.py runserver 0.0.0.0:8080

