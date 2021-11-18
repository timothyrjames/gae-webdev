import logging

from google.cloud import datastore


### Your data storage code goes here.
# Look at: https://console.cloud.google.com/datastore to see your live
# entities.


def get_client():
    # Note that if we want to specify a project here, we could do it like this:
    # return datastore.Client('your-project-id')
    # Calling Client() with no argument will access the environment variables
    # for your project.
    return datastore.Client()

