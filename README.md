django-h5bp
===========

A simple HTML5 Boilerplate Django app that has some predefined template Blocks,
useful to be extended in any application template.


Usage
-----------------------------------

Add this app to the 'installed_apps' settings:

    INSTALLED_APPS = (
        ...
        'django_h5bp',
    )

Extend the H5BP template in your base template, here is an example:

    {% extends "h5bp.html" %}

    {% block page-title %}My Great Project{% endblock %}

    {% block header %}
        <h1 class="title">Here is my page header</h1>
    {% endblock %}

    {% block main-container %}
        <div>
            <p>Hello World!</p>
        </div>
    {% endblock %}

    {% block footer %}
        <p>Footer</p>
    {% endblock %}

That should be enought to have your base.html using the HTML5 Boilerplate django template.

Static Files
-----------------------------------
The H5BP template comes with some JS in it, as well as the default css style, all of them are correctly configured in the template to use the {{ STATIC_URL }} tag.

The only one missing is the favicon.ico, that you should set your own (else it would the default one, depending on the position you put the app in the installed app list).


H5BP Template Blocks
-----------------------------------

Here are all the blocks that exist in the h5bp.html:

### \<head\>
* page-title
* meta-description
* meta-keywords
* meta-author
* meta-generator
* meta-extras
* css-extras

### \<body\>\<header\>
* header

### \<body\>\<div class="main"\>
* main-container

### \<body\>
* js-imports

### \<body\>\<script type="text/javascript"\>
* jquery-docready
* jquery-winload

### \<body\>\<script type="text/javascript"\>
* js-onpage

### \<body\>
* analytics

404 Page
-----------------------------------

This app also contains the HTML5 Boilerplate default 404 page, with no template tags.


LICENSE
=============
This software is distributed using MIT license, see LICENSE file for more details.
