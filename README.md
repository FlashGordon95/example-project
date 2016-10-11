### Basic Web Application Project Example
###### Data Representation and Querying Project 2016

This repository contains code and information for a third-year undergraduate project for the module **Data Representation and Querying**.
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie) in the Department of Computer Science and Applied Physics.
The lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io).

##### Project Overview
We have created a Single-Page Web Application (SPA) that lets users track their To-Dos.
This application was selected after some deliberation.
Initially, we considered three different applications:
1. A [ToDoListMe](http://todolistme.net/) alternative.
2. A [Pastebin](http://pastebin.com/) alternative.
3. A [Yelp](https://www.yelp.ie/) alternative.

In our early discussions, we excluded option 3 as it would be too difficult to construct in the short time we had to complete the project.
That left option 1 and 2.
We chose 2 after some consideration, as we were more interested in the idea.


##### Team Members
We elected to complete this project as a team.
The team members are:
- Seasca the dog
- Marco the dog
- Mog the cat
All team members contributed to all aspects of the project.
However, Seasca was given the lead in documentation, Marco the lead in Python coding, and Mog was given the lead in front-end development (HTML, CSS and JS) and user experience.

##### Meetings
Team meetings were held every Tuesday at 11am in the canteen at GMIT's Dublin Road campus for the duration of the project.
At these meetings, the management of the project was discussed, among other topics.
The project was divided into separate tasks, and each task was assigned to team members - usually on an individual basis.
At each meeting, Mog took notes using their laptop and assigned the tasks using GitHub Issues.


##### How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

We use the [sqlite3](https://docs.python.org/2/library/sqlite3.html) package for persistence in the application.
This must also be installed.
However, no further configuration our setup is required, as the database is fully contained in the db directory in this repository.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python webapp.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:4000/ .
