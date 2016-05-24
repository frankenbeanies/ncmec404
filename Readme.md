ncmec404
========

This project generates 404 pages using the [National Center for Missing and Exploited Children](http:/www.missingkids.org) dataset. It includes two pieces: 

* HTML 404 page
* Flask Webservice

License
-------

[MIT](https://github.com/frankenbeanies/deck/blob/master/LICENSE)

404.html
--------

To use 404.html in your own project, simply add it and link it in. It's that simple. There are no external dependencies, and JQuery is not required! The page is purposefully minimally styled, allowing you to integrate it into your existing site with little effort.

api
---

The api is built as a Flask (Python) web service. It is ready for instant deployment to a heroku instance. Endpoints may be added in the future, but once one is added to the main branch, it will not be removed. The current endpoints are as follows: 

>/query/*state_abbreviation*

This endpoint returns a list of up to 10 missing persons from the given state. state_abbreviation should be the capitalized two-letter abbreviation for a state, e.g. Connecticut = CT, New York = NY, etc.  