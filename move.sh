cd ~/redWine
python setup.py sdist
cp ./dist/redWine-0.4.tar.gz /home/nixo/onlineweb4/redWine-0.4.tar.gz
cd /home/nixo/onlineweb4
vagrant ssh -c "source /usr/local/bin/virtualenvwrapper.sh; workon onlineweb; pip uninstall -y redWine; pip install redWine-0.4.tar.gz;"
