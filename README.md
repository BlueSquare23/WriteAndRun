# Detect and Run Arbitrary Code!

Main Idea: Enter almost any arbitrary code into a textbox on the website and
have the webapp automatically detect, run, and return the code's output!

* [See it in action!](https://youtu.be/1vbKLqb0Lsw)

## Installation

Run the following to install the Flask app in your present working directory.

```
git clone https://github.com/BlueSquare23/WriteAndRun.git
cd WriteAndRun
virtualenv venv 		# Virtual Env Optional
source venv/bin/activate 	# Virtual Env Optional
pip3 install -r requirements.txt
```

After installing the app you'll need to obtain a free API key by [signing up
for an Algorithmia account here](https://teams.algorithmia.com/signup). Once
you have an API key from them you'll want to put it in a file named .env

* File: .env
```
ALGO_API_KEY=simX************************
```

## Overview

This Python Flask application is really just a wrapper for two API's that do
all the heavy lifting. 

* [First API](https://algorithmia.com/algorithms/PetiteProgrammer/ProgrammingLanguageIdentification)

The first API is from Algorithmia. Their API is used here to do the programming
language detection.

* [Second API](https://github.com/engineer-man/piston)

The second API is [Engineer Man's Piston
API](https://www.youtube.com/watch?v=SD4KgwdjmdI). This unique RCE API is used
to execute the code after its source language has been determined.

## Running the App

You can start the application just by running, `python app.py`. 

```
source venv/bin/activate        # Virtual Env Optional
python3 app.py
```

And then visit [http://localhost:5000/](http://localhost:5000/) in a browser to
use the app.

## Security and Bugs

If this app seems inherently insecure that's because it probably is. In theory,
all of the code entered into the site's textbox is sent to [Engineer Man's
Piston API](https://github.com/engineer-man/piston) and never run on the same
server as the flask app itself. But yeah a textbox on a website intended to run
code is a good target for H4xZ0rZ!

All that to say; Yee be warned! I would Not advise hosting this application on
the public internet! I may have created a leaky flask. I claim no liability. 

As for bugs my policy is, if it hurts when you do that don't do that.

Email all inquires to: [nudecelebsforfree@gmail.com](mailto:nudecelebsforfree@gmail.com)
