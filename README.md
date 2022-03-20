# Datascout

WIP. Web project for data visualization written in Flask.  Lots of
functionality is needed.  Currently working on the data visualization
engine, then I'll focus on the frontend (maybe find a framework).
Will work with user authentication and authorization later, core
functionality is a priority.

## Techstack

Currently uses Flask for the backend and Python for the data
manipulation engine.  Using Chart.js (through CDN) for data
visualization.

## Setup

You will need Python 3 and PIP for this project.
Refer to the proper documentation if needed:
https://flask.palletsprojects.com/en/2.0.x/

### Create and activate an environment

```
$ cd server/
$ python3 -m venv venv
$ . venv/bin/activate
```

### Install Flask through PIP and run project

```
$ pip install Flask python-dotenv
$ flask run
```

on localhost, go to `/graphs` to see the test data being shown using
Chart.js.
