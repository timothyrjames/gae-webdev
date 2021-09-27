# Logging and Debugging

This file illustrates the use of logging & debugging in Flask on Google App Engine.

A few differences from previous projects:

* In this project, we update ```requirements.txt``` to include the line ```google-cloud-logging``` - which will utilize the latest version of the cloud logging library.
* We ```import google.cloud.logging``` to use this when enabling Google Cloud Logging.
* When the /warn or /error pages are loaded, we write a message to the logs using standard Python logging. You can view these logs by navigating to [https://console.cloud.google.com/logs/viewer](https://console.cloud.google.com/logs/viewer).
