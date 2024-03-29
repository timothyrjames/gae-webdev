# First Deployment Tutorial

## Your First Google App Engine Project

This tutorial explains how to deploy your first application to Google App 
Engine. 


## Creating Your Python File

Start off by creating the following Python code into a `main.py` file. You can
edit it directly in the editor or you can use the command line editor of your 
choice; to open it in nano, use the following command:

```bash
nano main.py
```


**main.py**:
```python
import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return ('Hello, world! The time is %s' % datetime.datetime.now())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
```

## Creating Your Yaml File

Next, you'll want to do the same for app.yaml. 

```bash
nano app.yaml
```


**app.yaml**:
```yaml
runtime: python310

handlers:
- url: /.*
  script: auto
```


## Installing Flask

You'll want to start by installing Flask.

```bash
pip3 install Flask==2.1.0
```

Once you've got Flask installed, you can easily test your first application 
by running the following command.

```bash
python3 main.py
```

Your application can be tested by using the web preview; there's a button to 
open it in the top-right corner of your screen.


## Creating Your Application

If you haven't created a project yet, you can do that from the command line.

To create your project, enter the command below, but following "gcloud projects
create" you need to enter a project ID. It will need to be unique for all of
App Engine.

```bash
gcloud projects create 
```

If you _have_ created a project, you'll need to set it using the gcloud 
command - but enter _your_ project ID (instead of YOUR-APPLICATION-ID)
following the "gcloud config set project" text:

```bash
gcloud config set project YOUR-APPLICATION-ID
```


## Deploying Your Application

Note that we have to tell Google App Engine that we are using Flask; we do this
with the requirements.txt file.  You can see what it looks like with this
command:

```bash
nano requirements.txt
```

In this file, you'll add a single line:

```txt
flask==2.1.0
```

In the future, we'll be able to tell pip to install using the same format with
the -r flag.

```bash
pip3 install -r requirements.txt
```

Once you've done this, you can deploy easily:

```bash
gcloud app deploy
```


## Viewing your live application

Now you can find your application by navigating to the following URL in your 
browser: 

```
http://YOUR-APPLICATION-ID.appspot.com/ 
```

You can also enter the command below to view your live application:

```bash
gcloud app browse
```
