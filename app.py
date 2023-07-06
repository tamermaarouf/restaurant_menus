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
    return render_template('newRestaurant.html')

@app.route('/restaurant/new/', methods=['POST'])
def newRestaurant_submission():
    new_Restaurant = request.form['name']
    print(new_Restaurant)
    error_in_insert = False
    try:
        createRestaurant = Restaurant(name=new_Restaurant)
        db.session.add(createRestaurant)
        db.session.commit()
    except Exception as e:
        error_in_insert = True
        print(f'Exception "{e}" in create_restaurant_submission()')
        db.session.rollback()
        print(sys.exc_info())        
    finally:
        db.session.close()
    if error_in_insert:
        flash('An error occured. Restaurant ' + request.form['name'] + '  Could not be listed!!')
    else:
      flash('Restaurant ' + request.form['name'] + ' was successfully listed!')
    return redirect(url_for('showRestaurant'))

# Task 2: Create route for editRestaurant function here

@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    # return "page to edit Restaurant. Task 2 complete!"
    return render_template('editRestaurant.html')

# Task 3: Create a route for deleteRestaurant function here

@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET'])
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant.html')

@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['POST'])
def deleteRestaurant_submission(restaurant_id):
    # TODO: Complete this endpoint for taking a restaurant_id, and using
    # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
    delete_restaurant = Restaurant.query.get(restaurant_id)
    delete_name = delete_restaurant.name
    print(delete_name)
    error_in_insert = False
    try:
        db.session.delete(delete_restaurant)
        db.session.commit()
    except Exception as e:
        error_in_insert = True
        db.session.rollback()
    finally:
        db.session.close()
    if error_in_insert:
    # if error occur, error message pop up
        flash('An error occurred deleting restaurant' + delete_name)
    else:
    # if success, success message pop up
        flash('Successfully removed restaurant ' + delete_name)
    return redirect(url_for('showRestaurant'))

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
