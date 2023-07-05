# ------------------------> Imports <-----------------------------------
import os
import sys
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from database_setup import app, db, MenuItem, Restaurant


#------------------------> Controllers <-------------------
@app.route('/')
@app.route('/restaurant')
def restaurants():
    data = MenuItem.query.join(Restaurant).all()
    #data = Restaurant.query.order_by(Restaurant.name).all()
    return render_template('menu.html', restaurants=data)


# Task 1: Create route for newMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


#------------------------> Launch <------------------------------------
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 2023))
    app.run(host='0.0.0.0', port=port)
