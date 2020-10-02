Assignment: Semi-Restful Users 

Create an app that can handle all of the CRUD operations (create, read, update and destroy) for a table. Ensure that you add validation rules before saving the records in the database.

But first, what does REST mean? It's very common for a web application to provide the user interface for creating, reading, updating, or destroying a 'resource' (a table). For example, imagine you want to build a web application that allows the user to create/read/update/destroy users. There are many ways that you can build web applications like this. For example, you could have resources called users, products, pd (short for products) and so forth. You could also have different methods that essentially do the same thing. So, to display user information for user id 1, you could have the URL 'users/1' provide this info or 'users/show/1' or 'users/show_info/1' or 'users/display/1', etc.

Since many web applications perform CRUD operations, you can imagine how confusing this could get if everyone followed different conventions for creating routing and method names for these operations.

A REST or RESTful route is simply a set of route naming conventions that the industry has agreed to follow in order to make it easier to send requests to APIs. It's up to you whether you also follow these rules/conventions but we strongly encourage you to get familiar with the following rules for RESTful routing, as you may be making requests to, or someday creating your own, API.

Right now with Django, it's not quite possible for you to do the full RESTful architecture, so the exercise below is to help you get somewhat familiar with RESTful routes. Later when you get into other stacks (such as MEAN or Rails), you'll already be somewhat familiar with REST concepts.

Follow the instructions in the wireframe below to build this application in Django.




Notice that for every form submission we use a POST method, while we're rendering our templates from get routes.

Make sure to...

Complete each of the following routes:  
/shows/new- GET - method should return a template containing the form for adding a new TV show  
/shows/create - POST - method should add the show to the database, then redirect to /shows/<id>  
/shows/<id> - GET - method should return a template that displays the specific show's information 
/shows - GET - method should return a template that displays all the shows in a table  
/shows/<id>/edit - GET - method should return a template that displays a form for editing the TV show with the id specified in the url  
/shows/<id>/update - POST - method should update the specific show in the database, then redirect to /shows/<id>  
/shows/<id>/destroy - POST - method should delete the show with the specified id from the database, then redirect to /shows  
Have your root route redirect to /shows