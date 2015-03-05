#!/bin/sh

# Base directory
BASE_DIR=$(dirname $0)

# Virtualenv directory
VIRTUALENV_DIR="$BASE_DIR/env"

# Path to virtualenv pip
PIP_PATH="$VIRTUALENV_DIR/bin/pip"

# Requirements file
REQUIREMENTS_FILE="$BASE_DIR/requirements.txt"

VIRTUALENV=`which virtualenv`

echo $BASE_DIR
echo $VIRTUALENV_DIR
echo $REQUIREMENTS_FILE

install_requirements() {
    echo $BASEDIR
    # Create virtualenv directory
    if [ ! -d "$VIRTUALENV_DIR" ]; then
        $VIRTUALENV $VIRTUALENV_DIR
    fi
    # Install requirements using the virtualenv pip and the requirements.txt file
    $PIP_PATH install --upgrade -r $REQUIREMENTS_FILE
}

install_requirements

