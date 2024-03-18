# The Tree Survey is my solo project that I developed for Coding Dojo.

🌲 This project is a Python with Flask application. Using HTML5, CSS3, Jinja2, and Bootstrap for the Front-end work.

🌲 Back-end work consist of Python3 and MySQL. I used Balsamiq wireframes to draw up the page layout concepts.

🌲 Project Description: The Arbor Day Foundation sends me a paper survey each year asking questions. I was thinking of creating a webpage for folks to enter trees they have counted around them.

* - Register and Login page (with validation)<br>
* - Welcome dashboard page for user they can see what they have entered. Edit & Delete links<br>
* - Add location where they are at and how many trees are in that location. (address will have validations, # of trees etc)<br>
* - Edit page pre-fills data to edit.<br>
* - Tree look up page<br>


🌲 Backlog:

- Tree look up page may have to go into the backlog. I’d like to do a search for a tree based on selections they make and it returns different options to view and find the tree.  Or allowing the user to upload a photo and it returns a list of potential matches to view and choose from.

- Make another additional page that covers every question that is present on the paper version of the survey.

- Additional page for Tree companies doing work on planting more trees.

- Add page for Bird, butterfly, and wildlife conservation info.


🌲 New Programming Concept(s) I'm Planning to Learn: - Implement the Jinja2 "includes" into my html, and further work with Bootstrap (responsiveness).

## The requirements for the solo project that we had to meet are the following.
## Solo Project Proposal

🥷 It's time to start putting your bootcamp skills to something you want to share with the world!

🥷 Begin by coming up with an idea, either from the listed wireframes, or your own design.  Your project should NOT be related to a belt exam or a past full-stack assignment. Your project should advance yourself as a developer, and it can also:

    Relate to a passion or hobby of yours
    Solve or simplify a problem for yourself or somebody
    Perform common good for a community

The front-end/design of your project can be just as important as your back-end, make sure you allow yourself the time to focus on this as well.

You should then build up a feature list for what you would want to include in your presentation (Minimum Viable Product or MVP) and features that would be cool, but not crucial (product backlog).

Project Requirements

✓ - Required, these are mostly competencies that were required for your Orange/Red belt

B - Bonus, some are Black belt features, while others are within your abilities

| Language Used | PYTHON |
| ------------- |:-------------:|
| Project is on GitHub | ✓ |
| .gitignore file in root folder | ✓ |
| All of CRUD* on a non-User table (Create, Read, Update, Delete) | ✓ |
| CSS implemented, and possibly other static content | ✓ |
| Data is validated upon create and edit, errors show | ✓ |
| Login and Registration with validations | ✓ |
| Protected routes (Must be logged in to view) | ✓ |
| Application is responsive | B |
| Application uses a CSS framework such as Bootstrap | B |
| Application is publicly deployed | B |
| Application features a third-party API | B |
| File Upload | B |
| Many-to-many relationship (like, favorite, RSVP, etc) | B |
| AJAX | B |
| Project uses Django instead of Flask | B |

* - 

https://git-scm.com/docs/gitignore

https://www.toptal.com/developers/gitignore

🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷

## Login & Registration Page:

<a href="#"><img src="img/Login-Registration-Page.png" height="200" /></a>

## Login Validation:

<a href="#"><img src="img/Login-Validation.png" height="200" /></a>

## Registration Validation:

<a href="#"><img src="img/Registration-Validation.png" height="200" /></a>
<a href="#"><img src="img/Registration-Validation2.png" height="200" /></a>

## Dashboard (Home) Page:

<a href="#"><img src="img/Dashboard-Page.png" height="200" /></a>

## Add Location Page & Validation (Create/Insert):

<a href="#"><img src="img/Add-Location-Page.png" height="200" /></a>
<a href="#"><img src="img/Add-Location-Validation.png" height="200" /></a>

## View Location Page & Edit Location Page (Read/Select & Update):

<a href="#"><img src="img/View-Location-Page.png" height="200" /></a>
<a href="#"><img src="img/Edit-Location-Page.png" height="200" /></a>

### Delete link is listed on the Dashboard page.

## Instructions: (Note: these instructions are for a Mac.)
You will have to forward engineer the ERD and run 'pipenv install PyMySQL flask flask-bcrypt' after downloading the files.
pipenv shell
python3 server.py
Open Local host in your browser.
