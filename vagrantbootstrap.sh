#!/bin/bash


LJUST_COLS=20
RJUST_COLS=30
VERBOSE=false
RUNSERVER=false


function init() {
    printf "\n\nVERBOSE = $VERBOSE, toggle in vagrantbootstrap.sh\n\n"
    sleep 1

    echo "killing running dev servers"
    pkill -9 -f "python manage.py"
}

function progress() {
    if $VERBOSE
    then
        $@
    else
        cmd="$@"
        $@ &> /dev/null &
        pid=$!
        spinner='-\|/'

        i=0
        while kill -0 $pid &> /dev/null
        do
            i=$(( (i+1) %4 ))
            printf "\r\t%-${LJUST_COLS}.${LJUST_COLS}s %${RJUST_COLS}s" "${cmd}" "[ ${spinner:$i:1}${spinner:$i:1} ]"
            sleep .1
        done

        if [ $? -ne 0 ]
        then
            echo "return code $?";
        fi
        printf "\r\t%-${LJUST_COLS}.${LJUST_COLS}s %${RJUST_COLS}s\n" "${cmd}" "[ OK ]"
    fi
}



function update_packages() {
    echo "updating packages"
    progress sudo apt-get update
}

function install_packages() {
    echo "installing packages"
    progress sudo apt-get install -y \
        python-dev python-setuptools python-virtualenv vim \
        tmux screen git-core curl build-essential openssl \
        libssl-dev
}

function setup_virtualenv() {
    echo "installing virtualenvwrapper"
    # use pip to install globally, installing with apt doesn't create the shellscript for sourcing
    progress sudo pip install virtualenvwrapper
    source /usr/local/bin/virtualenvwrapper.sh

    if ! grep -q "source /usr/local/bin/virtualenvwrapper.sh" .bashrc; then
        echo "adding script to .bashrc"
        echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
    fi

    echo "creating virtualenv"
    progress mkvirtualenv redwine
}

function install_onlineweb_requirements() {
    echo "installing onlineweb requirements"
    workon redwine
    cd /vagrant
    progress pip install -r requirements.txt
}

function prepare_and_run_onlineweb() {
    workon redwine
    cd /vagrant
    cp onlineweb4/settings/example-local.py onlineweb4/settings/local.py
    echo "creating tables"
    progress python manage.py syncdb
    if $RUNSERVER
    then
        echo "starting dev server"
        python manage.py runserver 0.0.0.0:8000 &
        echo "done, check http://localhost:8001 on host"
    fi
}

init
update_packages
install_packages
setup_virtualenv
install_onlineweb_requirements
