# ------------------------> Imports <-----------------------------------
import os
import sys
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from database_setup import app, db, MenuItem, Restaurant


#------------------------> Controllers <-------------------
@app.route('/restaurant')
def restaurant():
    restaurant_query = Restaurant.query.order_by(Restaurant.name).all()

#------------------------> Launch <------------------------------------
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 2023))
    app.run(host='0.0.0.0', port=port)
