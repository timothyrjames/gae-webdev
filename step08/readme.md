# CSS Examples

This project illustrates the use of CSS.

A few notable changes in this project from previous projects:

* In ```main.py``` we are using URL parameterization ```@app.route('/p/<requested_page>')``` to receive a particular page as a parameter to our function so that we can process all template requests with a single function.
* Our ```_base.html``` template includes the line ```<link rel="stylesheet" href="/s/style.css">``` to include our CSS stylesheet from our static files folder.
* Our ```style.css``` file includes several selectors to demonstrate how CSS can be applied.
* A new ```absolutes.html``` HTML file has been added to illustrate the use of absolute positioning.
* Most HTML files have not be significantly modified, but due to the use of our CSS file, you'll see lots of visual differences, especially in ```tables.html``` and ```sections.html```.

It would be an interesting exercise to review the HTML in step05 and see the
differences when CSS is applied.
