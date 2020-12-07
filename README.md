# APP NAME
Plandrel Blog Website
# AUTHOR
Tabitha Wanjiku

# DESCRIPTION
This is an app to create a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users. 


# User Stories
A users can see blogs that other people have posted

A user can comment on different blogs and leave feedback

A user can see random quotes displayed once the page is refreshed

A writer can submit a blog post

A writer can delete comments that are insulting to their blog

A writer can update the blog they posted

# BDD
Behaviour	         |    Input	                     |           Output

---------------------+-------------------------------+-------------------------------

Create an account    | Click Register                |Register a new user

---------------------|-------------------------------|------------------------------

Go to your previous  |Click login                    |Return to your previous account
account

---------------------|-------------------------------|--------------------------------

See your profile     |Click profile                  |See your bio and profile pic

---------------------|-------------------------------|-------------------------------

Go to main page      |Click home                     |Go back to homepage

# Prerequisites
Python3.6

# Installation steps
$ git clone https://github.com/tw8130/BLOG-WEB.git

$ cd Blog

$ source virtual/bin/activate

Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')

$ ./start.sh

# How it works
A user needs to sign up

A user the needs to sign in order to see posts,create posts,comment posts and delete posts

# Technologies Used
This project uses major technologies which are :

HTML5/CSS

Bootstrap

Python3.6

flask

## KNOWN BUGS:
Any bugs noted you can email me for clarification.

## CONTACT INFO:
You can email at:mwangitabitha2020@gmail.com

## LICENSE:
MIT License

Copyright (c) [2020] Tabitha Wanjiku]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.