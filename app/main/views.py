from flask import  render_template,redirect,request,url_for,abort,flash
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Blogr - Welcome to my blog'

    return render_template('index.html', title=title)