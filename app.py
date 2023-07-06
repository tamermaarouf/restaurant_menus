# ------------------------> Imports <-----------------------------------
import os
import sys
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from database_setup import app, db, MenuItem, Restaurant


#------------------------> Controllers <-----------------------------------------------------------------------#
@app.route('/')
@app.route('/restaurant')
def showRestaurant():
    data = Restaurant.query.order_by(Restaurant.name).all()
    return render_template('index.html', restaurants=data)

# Restaurant
#---------------------------------------------------------------------------------------------------
# Task 1: Create route for newRestaurant function here
@app.route('/restaurant/new/', methods=['GET'])
def newRestaurant():    
    # return "page to create a new Restaurant. Task 1 complete!"
    return render_template('newRestaurant.html')

@app.route('/restaurant/new/', methods=['POST'])
def newRestaurant_submission():    
    # return "page to create a new Restaurant. Task 1 complete!"
    return redirect(url_for('showRestaurant'))

# Task 2: Create route for editRestaurant function here

@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    # return "page to edit Restaurant. Task 2 complete!"
    return render_template('editRestaurant.html')

# Task 3: Create a route for deleteRestaurant function here

@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    # return "page to delete a Restaurant. Task 3 complete!"
    return render_template('deleteRestaurant.html')

@app.route('/menu')
@app.route('/menu/<int:restaurant_id>')
def menu(restaurant_id):
    data = MenuItem.query.filter(MenuItem.restaurant_id==restaurant_id)
    restaurant_name = Restaurant.query.get(restaurant_id)
    return render_template('menu.html', restaurants=data, name=restaurant_name)


# Task 1: Create route for newMenuItem function here
@app.route('/menu/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):    
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here

@app.route('/menu/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/menu/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


#------------------------> Launch <------------------------------------
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 2023))
    app.run(host='0.0.0.0', port=port)
