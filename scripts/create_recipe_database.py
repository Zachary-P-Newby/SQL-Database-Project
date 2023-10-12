import sqlite3

connection = sqlite3.connect("..\databases\\cookbook.db")
cursor = connection.cursor()

#cursor.execute("""
#CREATE TABLE recipes (
#               id INTEGER PRIMARY KEY, 1
#               author text, 2
#               name text, 3
#               source text, 4
#               searchIngredients text, 5
#               ingredients text, 6
#               totalTime text, 7
#               vegan text, 8
#               meat text, 9
#               fish text, 10 
#               dairy text,11
#               wheat text, 12
#               egg text, 13
#               directions text, 14
#               nutritionFacts text 15)
#""")


cursor.execute("""INSERT INTO recipes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
               (2,
                "Tarryn",
                "Easy Baked Chicken Tenders",
                "https://www.allrecipes.com/recipe/273852/easy-baked-chicken-tenders/",
                "cooking spray|egg|panko bread crumbs|garlic powder|onion powder|paprika|salt|black pepper|chicken",
                """cooking spray
1 large egg, beaten
1 ¼ cups panko bread crumbs
2 teaspoons garlic powder
1 teaspoon onion powder
1 teaspoon ground paprika
1 teaspoon kosher salt
1 teaspoon ground black pepper
4 skinless, boneless chicken tenders, cut into 1/2-inch strips lengthwise""",
                "30 minutes",
                "No",
                "Yes",
                "No",
                "No",
                "Yes",
                "Yes",
                """(1. Gather all ingredients.
(2. Preheat the oven to 450 degrees F (230 degrees C). Line a baking sheet with aluminum foil and spray with cooking spray.
(3. Place egg in a shallow dish. Place panko, garlic powder, onion powder, paprika, salt, and pepper into a large zip-top freezer bag and mix well.
(4. Dip 2 chicken strips into egg, then place into panko mixture and shake to coat. Place coated chicken pieces onto the prepared baking sheet. Repeat with remaining chicken.
(5. Spray each chicken tender with cooking spray twice.
(6. Bake tenders in the preheated oven for 7 minutes. Flip and continue to bake on opposite side until no longer pink in the centers, about 7 minutes more. Remove from the oven.
(7. Set an oven rack about 6 inches from the heat source and preheat the oven's broiler.
(8.  Broil tenders in the preheated oven for extra crunch, about 1 to 2 minutes more.
(9. Serve hot and enjoy!""",
                """Calories 172
Fat 4g
Sodium 689mg
Carbs 26g
Fiber 1g
Sugars 1g 
Protein 17g
"""
            ))

cursor.execute("""INSERT INTO recipes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
               (3,
                "g0dluvsugly",
                "Simple Macaroni and Cheese",
                "https://www.allrecipes.com/recipe/238691/simple-macaroni-and-cheese/",
                "macaroni|butter|flour|salt|black pepper|milk|cheddar cheese",
                """1 (8 ounce) box elbow macaroni
¼ cup butter
¼ cup all-purpose flour
½ teaspoon salt
ground black pepper to taste
2 cups milk
2 cups shredded Cheddar cheese""",
                "25 minutes",
                "No",
                "No",
                "No",
                "Yes",
                "Yes",
                "No",
                """(1. Bring a large pot of lightly salted water to a boil. Cook elbow macaroni in the boiling water, stirring occasionally until cooked through but firm to the bite, 8 minutes.
(2. At the same time, melt butter in a saucepan over medium heat.
(3. Add flour, salt, and pepper and stir until smooth, about 5 minutes.
(4. Pour in milk slowly, while stirring continuously. Continue to cook and stir until mixture is smooth and bubbling, about 5 minutes, making sure the milk doesn't burn.
(5. Add Cheddar cheese and stir until melted, 2 to 4 minutes.
(6. Drain macaroni and fold into cheese sauce until coated.
(7. Serve hot and enjoy!""",
                """Calories 630
Fat 34g
Sodium 777mg
Carbs 55g
Fiber 2g
Sugars 8g
Protein 27g
"""
            ))


cursor.execute("""INSERT INTO recipes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
               (4,
                "elohel",
                "Buttered Noodles",
                "https://www.allrecipes.com/recipe/244458/buttered-noodles/",
                "fettuccine noodles|butter|parmesan cheese|salt|black pepper",
                """1 (16 ounce) package fettuccine noodles
6 tablespoons butter, cut into pieces
⅓ cup grated Parmesan cheese
salt and ground black pepper to taste""",
                "20 minutes",
                "No",
                "No",
                "No",
                "Yes",
                "Optional",
                "No",
                """(1. Gather all ingredients.
(2. Fill a large pot with lightly salted water and bring to a rolling boil.
(3. Stir in fettuccine, bring back to a boil, and cook pasta over medium heat until tender yet firm to the bite, 8 to 10 minutes.
(4. Drain and return pasta to pot. Mix butter, Parmesan cheese, salt, and pepper into pasta until evenly combined.
(5.Serve hot and enjoy!""",
                """Calories 294
                Fat 11g
                Sodium 135mg 
                Carbs 41g  
                Fiber 2g
                Sugars 2g
                Protein 9g"""
            ))


cursor.execute("""INSERT INTO recipes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
               (5,
                "Nicole Burdett",
                "Simple Broiled Haddock",
                "https://www.allrecipes.com/recipe/232906/simple-broiled-haddock/",
                "haddock|onion powder|paprika|garlic powder|black pepper|salt|cayenne pepper|butter|lemon",
                """2 pounds haddock fillets
½ teaspoon onion powder
½ teaspoon paprika
½ teaspoon garlic powder
½ teaspoon ground black pepper
½ teaspoon salt
¼ teaspoon cayenne pepper
1 tablespoon butter, cut in small pieces
1 lemon, cut into wedges""",
                "20 minutes",
                "No",
                "No",
                "Yes",
                "Yes",
                "No",
                "No",
                """(1. Set an oven rack about 6 inches from the heat source and preheat the oven's broiler. Line a baking sheet with aluminum foil; spray with cooking spray.
(2. Arrange haddock fillets on the prepared baking sheet.
(3. Mix onion powder, paprika, garlic powder, black pepper, salt, and cayenne pepper in a small bowl; sprinkle seasoning over fish, then dot with butter.
(4. Broil in the preheated oven until fish flakes easily with a fork, 6 to 8 minutes. Serve with lemon wedges.""",
                """Calories 229
                Fat 5g
                Sodium 466mg
                Carbs 1g
                Fiber 0g
                Sugar 0g
                Protein 43g
"""
            ))

#cursor.execute("SELECT ingredients FROM recipes WHERE rowid == 1")
#result = cursor.fetchone()[0]
#print(result)
#Update Basic biiscuits searchIngredients
connection.commit()

print("Great success!")

connection.close()

#cursor.execute("""INSERT INTO recipes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
#               (1,
#                "",
#                "",
#                "",
#                "",
#                """""",
#                "",
#                "",
#                "",
#                "",
#                "",
#                "",
#                "",
#                """""",
#                """
#"""
#            ))