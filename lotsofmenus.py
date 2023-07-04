from database_setup import app
from database_setup import Restaurant, db, MenuItem
from flask_migrate import Migrate
from flask import Flask

'''
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
'''
with app.app_context():
  # db.drop_all()
  # Menu for UrbanBurger
  restaurant1 = Restaurant(name="Urban Burger")

  menuItem1 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                         price="$7.50", course="Entree", restaurants=restaurant1)

  menuItem2 = MenuItem(name="French Fries", description="with garlic and parmesan", 
                         price="$2.99", course="Appetizer", restaurants=restaurant1)

  menuItem3 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                         price="$5.50", course="Entree", restaurants=restaurant1)

  menuItem4 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream", 
                         price="$3.99", course="Dessert", restaurants=restaurant1)

  menuItem5 = MenuItem(name="Sirloin Burger", description="Made with grade A beef", 
                         price="$7.99", course="Entree", restaurants=restaurant1)

  menuItem6 = MenuItem(name="Root Beer", description="16oz of refreshing goodness", 
                         price="$1.99", course="Beverage", restaurants=restaurant1)

  menuItem7 = MenuItem(name="Iced Tea", description="with Lemon", 
                         price="$.99", course="Beverage", restaurants=restaurant1)

  menuItem8 = MenuItem(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                         price="$3.49", course="Entree", restaurants=restaurant1)

  menuItem9 = MenuItem(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                         price="$5.99", course="Entree", restaurants=restaurant1)


    # Menu for Super Stir Fry
  restaurant2 = Restaurant(name="Super Stir Fry")

  menuItem10 = MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                         price="$7.99", course="Entree", restaurants=restaurant2)

  menuItem11 = MenuItem(name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", 
                         price="$25", course="Entree", restaurants=restaurant2)

  menuItem12 = MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                         price="15", course="Entree", restaurants=restaurant2)

  menuItem13 = MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                         price="12", course="Entree", restaurants=restaurant2)

  menuItem14 = MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                         price="14", course="Entree", restaurants=restaurant2)

  menuItem15 = MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                         price="12", course="Entree", restaurants=restaurant2)


    # Menu for Panda Garden
  restaurant3 = Restaurant(name="Panda Garden")


  menuItem16 = MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                         price="$8.99", course="Entree", restaurants=restaurant3)

  menuItem17 = MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                         price="$6.99", course="Appetizer", restaurants=restaurant3)

  menuItem18 = MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                         price="$9.95", course="Entree", restaurants=restaurant3)

  menuItem19 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                         price="$6.99", course="Entree", restaurants=restaurant3)

  menuItem20 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                         price="$9.50", course="Entree", restaurants=restaurant3)


    # Menu for Thyme for that
  restaurant4 = Restaurant(name="Thyme for That Vegetarian Cuisine ")


  menuItem21 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                         price="$2.99", course="Dessert", restaurants=restaurant4)

  menuItem22 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                         price="$5.99", course="Entree", restaurants=restaurant4)

  menuItem23 = MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                         price="$4.50", course="Dessert", restaurants=restaurant4)

  menuItem24 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                         price="$6.95", course="Appetizer", restaurants=restaurant4)

  menuItem25 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                         price="$7.95", course="Entree", restaurants=restaurant4)

  menuItem26 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                         price="$6.80", course="Entree", restaurants=restaurant4)


    # Menu for Tony's Bistro
  restaurant5 = Restaurant(name="Tony\'s Bistro ")


  menuItem27 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                         price="$13.95", course="Entree", restaurants=restaurant5)

  menuItem28 = MenuItem(name="Chicken and Rice", description="Chicken... and rice",
                         price="$4.95", course="Entree", restaurants=restaurant5)

  menuItem29 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                         price="$6.95", course="Entree", restaurants=restaurant5)

  menuItem30 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                         description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert", restaurants=restaurant5)

  menuItem31 = MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                         price="$7.95", course="Entree", restaurants=restaurant5)

    # Menu for Andala's
  restaurant6 = Restaurant(name="Andala\'s")

  menuItem32 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                         price="$9.95", course="Entree", restaurants=restaurant6)

  menuItem33 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                         price="$7.95", course="Entree", restaurants=restaurant6)

  menuItem34 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                         price="$6.50", course="Appetizer", restaurants=restaurant6)

  menuItem35 = MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                         price="$6.75", course="Appetizer", restaurants=restaurant6)

  menuItem36 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                         price="$7.00", course="Entree", restaurants=restaurant6)


    # Menu for Auntie Ann's
  restaurant7 = Restaurant(name="Auntie Ann\'s Diner ")

  menuItem37 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                         price="$8.99", course="Entree", restaurants=restaurant7)


  menuItem38 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                         price="$2.99", course="Dessert", restaurants=restaurant7)

  menuItem39 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                         price="$10.95", course="Entree", restaurants=restaurant7)

  menuItem40 = MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                         price="$7.50", course="Appetizer", restaurants=restaurant7)

  menuItem41 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                         price="$8.95", course="Entree", restaurants=restaurant7)

  menuItem42 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                         price="$9.50", course="Entree", restaurants=restaurant7)

  menuItem43 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                          price="$1.99", course="Dessert", restaurants=restaurant7)


    # Menu for Cocina Y Amor
  restaurant8 = Restaurant(name="Cocina Y Amor ")

  menuItem44 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                         price="$5.95", course="Entree", restaurants=restaurant8)

  menuItem45 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                         price="$7.99", course="Entree", restaurants=restaurant8)


  restaurant9 = Restaurant(name="State Bird Provisions")

  menuItem46 = MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                         price="$5.95", course="Appetizer", restaurants=restaurant9)

  menuItem47 = MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                         price="$6.95", course="Dessert", restaurants=restaurant9)


  menuItem48 = MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                         price="$4.25", course="Dessert", restaurants=restaurant9)

  db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5, restaurant6, restaurant7, restaurant8, restaurant9])
  db.session.add_all([menuItem1, menuItem2, menuItem3, menuItem4, menuItem5, menuItem6, menuItem7, menuItem8, menuItem9, menuItem10])
  db.session.add_all([menuItem11, menuItem12, menuItem13, menuItem14, menuItem15, menuItem16, menuItem17, menuItem18, menuItem19])
  db.session.add_all([menuItem20, menuItem21, menuItem22, menuItem23, menuItem24, menuItem25, menuItem26, menuItem27, menuItem28])
  db.session.add_all([menuItem29, menuItem30, menuItem31, menuItem32, menuItem33, menuItem34, menuItem35, menuItem36, menuItem37])
  db.session.add_all([menuItem38, menuItem39, menuItem40, menuItem41, menuItem42, menuItem43, menuItem44, menuItem45, menuItem46])
  db.session.add_all([menuItem47, menuItem48])
  db.session.commit()

  print("added menu items!")
