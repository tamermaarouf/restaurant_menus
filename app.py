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

@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET'])
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['POST'])
def editRestaurant_submission(restaurant_id):
    edit_restaurant = Restaurant.query.get(restaurant_id)
    error_in_insert = False
    try:
        edit_restaurant.name = request.form['name']
        db.session.commit()
    except Exception as e:
        error_in_insert = True
        db.session.rollback()
        print(e)
        print(sys.exc_info())
    finally:
        db.session.close()
    if error_in_insert:
        flash('An error occurred. Restaurant could not be updated')
    else:
        flash('Restaurant was successfully updates')
    return redirect(url_for('showRestaurant'))

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
@app.route('/menu/<int:restaurant_id>/new/', methods=['GET'])
def newMenuItem(restaurant_id):
    return render_template('newmenuitem.html')
    # return "page to create a new menu item. Task 1 complete!"

@app.route('/menu/<int:restaurant_id>/new/', methods=['POST'])
def newMenuItem_submission(restaurant_id):
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    course = request.form.get('course')
    error_in_insert = False
    try:
        createMenuItem = MenuItem(name=name, description=description, 
                                  price=price, course=course, restaurant_id=restaurant_id)
        db.session.add(createMenuItem)
        db.session.commit()
    except Exception as e:
        error_in_insert = True
        print(f'Exception "{e}" in newMenuItem_submission')
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if error_in_insert:
            flash('An error occurred. Menu Item' + request.form['name'] + 'could not be listed.')
        else:
            flash('Menu Item' + request.form['name'] + 'was successfully listed!')
    return redirect(url_for('showRestaurant'))
    # return "page to create a new menu item. Task 1 complete!"



# Task 2: Create route for editMenuItem function here

@app.route('/menu/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/menu/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET'])
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deletemenuitem.html')

@app.route('/menu/<int:restaurant_id>/<int:menu_id>/delete/', methods=['POST'])
def deleteMenuItem_submission(restaurant_id, menu_id):
    deleteMenuItem = MenuItem.query.get(menu_id)
    deleteName = deleteMenuItem.name
    error_in_delete = False
    try:
        db.session.delete(deleteMenuItem)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        error_in_delete = True
    finally:
        db.session.close()
    if error_in_delete:
        flash('An error occurred deleting Menu Item' + deleteName)
    else:
        flash('Successfully removed Menu Item' + deleteName)
    return redirect(url_for('showRestaurant'))


#------------------------> Launch <------------------------------------
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 2023))
    app.run(host='0.0.0.0', port=port)
