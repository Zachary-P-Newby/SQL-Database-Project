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
               (1,
                "lenihan5",
                "Basic Biscuits",
                "https://www.allrecipes.com/recipe/20075/basic-biscuits/",
                "Flour|Baking Powder|Salt|Shortening|Milk",
                """2 cups all-purpose flour\n1 tablespoon baking powder\n½ teaspoon salt\n½ cup shortening\n¾ cup cold milk""",
                "25 minutes",
                "No",
                "No",
                "No",
                "Yes",
                "Yes",
                "No",
                """
(1. Gather all ingredients and preheat oven to 450 degrees F (230 degrees C).
(2. In a large mixing bowl sift together flour, baking powder and salt. Cut in shortening with fork or pastry blender until mixture resembles coarse crumbs.
(3. Pour milk into flour mixture while stirring with a fork. Mix in milk until dough is soft, moist and pulls away from the side of the bowl.
(4. Turn dough out onto a lightly floured surface and knead dough briefly, 5 to 7 times.
(5. Roll dough out into a 1/2 inch thick sheet and cut out biscuits with a floured cookie cutter. Press together unused dough and repeat rolling and cutting procedure.
(6. Place biscuits on ungreased baking sheets and bake in preheated oven until golden brown, about 10 minutes.
(7. Enjoy!
""",
                """
Calories 191,
Fat 11g
Sodium 225mg
Carbs 20g
Fiber 1g
Sugars 1g
Protein 3g
"""
            ))

cursor.execute("SELECT * FROM recipes")
print(cursor.fetchone())

connection.commit()

print("Great success!")

connection.close()