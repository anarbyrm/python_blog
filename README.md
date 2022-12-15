# Python Blog Project


# Description

<h4><em>This blog project is scripted for sharing Python related articles and tutorials. All posts are created by stuff users and there is no authentication required. It is for the sake of simplicity to reach a desired content. There are lots of blogs like this but it differs in some features. This blog designed to be in Azerbaijani language to help newcomers who only speak Azerbaijani to dive into Python with ease.</em></h4>


# Features

###### - Searching and filtering articles and tutorials
###### - Post read time
###### - Post viewers count based on IP addresses
###### - Completed status for tutorials


# How to configure locally

Follow the steps below..

## 1) Setup project requirements
For starters create virtual environment:

<code>$python3 -m venv venv </code>

Then download required packages from the requirements.txt with help of pip

<code>$python3 -m pip install -r requirements.txt</code>

## 2) Run project with the docker-compose file
Be aware to be in the same folder with docker-compose file

<code>$docker-compose up --build</code>

That is it! Now, you just need to go to <a href="0.0.0.0:8000" target="_blank">0.0.0.0:8000</a>


