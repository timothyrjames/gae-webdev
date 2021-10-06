# Flask Templates

This project illustrates the use of Flask Templates.

Note that for this project, we will create a folder called "templates" that will
include our Flask template files. These will look like ordinary HTML files, for
the most part - except they will include ```{%``` and ```%}``` characters, as
well as ```{{``` and ```}}``` characters. Code in these sections will be
interpreted on the *server* - when your browser receives the HTML, these
sections will be missing; they will have been interpreted at the server and the
results will be sent to the browser.

Another difference in this project from previous projects is the number and path
of routes; you can see many more routes being handled in this example (mapping
requests to view HTML to these functions) which will render a Flask template in
response.
