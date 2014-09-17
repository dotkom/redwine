cd ~/redwine
python setup.py sdist
cp ./dist/redwine-0.5.tar.gz /home/nixo/onlineweb4/redwine.tar.gz
cd /home/nixo/onlineweb4
vagrant ssh -c "source /usr/local/bin/virtualenvwrapper.sh; workon onlineweb; pip uninstall -y redwine; pip install redwine.tar.gz;"
