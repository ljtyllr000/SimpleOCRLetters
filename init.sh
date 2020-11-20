#!/bin/bash

# create database
python3 db_init.py

# migrate db
python3 manage.py makemigrations
python3 manage.py migrate

# create superuser
python3 superuser_init.py