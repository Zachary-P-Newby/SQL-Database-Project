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


recipies = [(9,
                "Chris Simpler",
                "Traditional Sauerbraten",
                "https://www.allrecipes.com/recipe/221361/traditional-sauerbraten/",
                "beef|onion|red wine vinegar|water|salt|black pepper|white sugar|clove|bay leaves|flour|vegetable oil|gingersnap cookies",
                """3 pounds beef rump roast
2 large onions, chopped
1 cup red wine vinegar, or to taste
1 cup water
1 tablespoon salt
1 tablespoon ground black pepper
1 tablespoon white sugar
10 whole cloves, or more to taste
2 bay leaves, or more to taste
2 tablespoons all-purpose flour
salt and ground black pepper to taste
2 tablespoons vegetable oil
10 gingersnap cookies, crumbled""",
                "2 days 4 hrs 15 mins",
                "No",
                "Yes",
                "No",
                "Yes",
                "Yes",
                "No",
                """(1. Place beef rump roast, onions, vinegar, water, 1 tablespoon salt, 1 tablespoon black pepper, sugar, cloves, and bay leaves in a large pot. Cover and refrigerate for 2 to 3 days, turning meat daily. Remove meat from marinade and pat dry with paper towels, reserving marinade.
                (2. Season flour to taste with salt and black pepper in a large bowl. Sprinkle flour mixture over beef.
                (3. Heat vegetable oil in a large Dutch oven or pot over medium heat; cook beef until brown on all sides, about 10 minutes.
                (4. Pour reserved marinade over beef, cover, and reduce heat to medium-low. Simmer until beef is tender, 3 1/2 to 4 hours.
                (5.Remove beef to a platter and slice.
                (6.Strain solids from remaining liquid and continue cooking over medium heat. Add gingersnap cookies and simmer until gravy is thickened, about 10 minutes. Serve gravy over sliced beef.""",
                """Calories 456
Fat 22g
Sodium 1683mg
Carbs 21g
Fiber 2g
Sugars 8g
Protein 41g"""
            ),
            (10,
                "Loves2CookinMN",
                "Wiener Schnitzel",
                "https://www.allrecipes.com/recipe/78117/wienerschnitzel/",
                "veal|flour|egg|parmesan cheese|milk|parsely|salt|pepper|nutmeg|bread crumbs|butter|lemon",
                """1 ½ pounds veal cutlets
½ cup all-purpose flour
2 large eggs
3 tablespoons grated Parmesan cheese
2 tablespoons milk
1 teaspoon minced parsley
½ teaspoon salt
¼ teaspoon pepper
1 pinch ground nutmeg
1 cup dry bread crumbs
6 tablespoons butter
4 slices lemon""",
                "1 hr 30 mins",
                "No",
                "Yes",
                "No",
                "Yes",
                "Yes",
                "Yes",
                """(1. Place veal cutlets between 2 sheets of heavy plastic on a solid, level surface. Firmly pound cutlets with the smooth side of a meat mallet to a 1/4-inch thickness. Dip cutlets in flour to coat; shake off excess.
(2. Beat together eggs, Parmesan cheese, milk, parsley, salt, pepper, and nutmeg in a shallow bowl until combined. Place bread crumbs on a plate. Dip each cutlet into the egg mixture, then press in bread crumbs to coat. Place coated cutlets on a plate and refrigerate for 1 hour to overnight.
(3. Melt butter in a large skillet over medium heat. Cook breaded cutlets in butter until browned, about 3 minutes per side. Transfer cutlets to a serving platter and pour pan juices over them. Garnish with lemon slices.""",
                """(1. Place veal cutlets between 2 sheets of heavy plastic on a solid, level surface. Firmly pound cutlets with the smooth side of a meat mallet to a 1/4-inch thickness. Dip cutlets in flour to coat; shake off excess.
(2. Beat together eggs, Parmesan cheese, milk, parsley, salt, pepper, and nutmeg in a shallow bowl until combined. Place bread crumbs on a plate. Dip each cutlet into the egg mixture, then press in bread crumbs to coat. Place coated cutlets on a plate and refrigerate for 1 hour to overnight.
(3. Melt butter in a large skillet over medium heat. Cook breaded cutlets in butter until browned, about 3 minutes per side. Transfer cutlets to a serving platter and pour pan juices over them. Garnish with lemon slices."""
            ),
            (11,
                "Alvin Zhou",
                "Scalloped Potatoes",
                "https://tasty.co/recipe/scalloped-potatoes",
                "butter|garlic|flour|milk|salt|pepper|yukon potato|parmesan cheese",
                """for 2 servings
1 tablespoon butter
2 cloves garlic
1 tablespoon flour
1 cup milk
1 teaspoon salt
½ teaspoon pepper
3 yukon potatoes, peeled
2 tablespoons grated parmesan cheese
fresh parsley, chopped, for garnish""",
                "1 hr 20 min",
                "No",
                "No",
                "No",
                "Yes",
                "Yes",
                "No",
                """(1. Preheat oven to 350°F (180°C).
(2. In a small pot, melt the butter and fry the garlic until it’s just starting to brown. Add the flour, salt and pepper. whisk until there are no lumps.
(3. Slowly drizzle in the milk while constantly whisking to make sure the mixture is smooth.
(4. Bring to a boil, then remove from heat.
(5. Slice the potatoes into about ⅛-inch (3 mm) thick slices, then fan them out in a small baking dish.
(6. Pour the sauce on top of the potatoes, then sprinkle with parmesan.
(7. Bake for about 1 hour, until the top is bubbly and golden brown.
(8. Sprinkle chopped parsley on top, then serve.
(9. Enjoy!""",
                """Unavailable"""
            ),
            (12,
                "Claire Nolan",
                "Easy Fish Tacos",
                "https://tasty.co/recipe/easy-fish-tacos",
                "cabbage|red onion|sour cream|lime|salt|tilapia|cayenne pepper|garlic powder|cumin|salt|pepper|tortilla|cilantro",
                """for 8 servings

CABBAGE SLAW
3 cups green cabbage, shredded
½ cup red onion, diced
1 cup sour cream
1 lime, juiced
¼ teaspoon salt

TACOS
4 tilapia fillets
¼ teaspoon cayenne pepper, ground
½ teaspoon garlic powder
½ teaspoon cumin
½ teaspoon salt
½ teaspoon pepper
16 corn tortillas

GARNISH
cilantro, to taste
lime, to taste""",
                "30 minutes",
                "No",
                "No",
                "Yes",
                "Yes",
                "Optional",
                "No",
                """(1. In a large bowl, combine green cabbage, red onion, sour cream, lime juice, and salt. Chill until ready to serve.
(2. In a bowl, mix cayenne, garlic powder, cumin, salt, and pepper. Season each tilapia fillet on both sides with the seasoning mix.
(3. Over medium-high heat, cook 2 fillets at a time for 8 minutes, flipping halfway. Repeat for the remaining fillets.
(4. Using a fork, break apart the fillets into bite-size pieces.
(5. Right before serving, heat the corn tortillas in the pan over high heat. Remove from the pan and assemble the tacos with the cabbage slaw and tilapia.
(6. Garnish with cilantro and lime juice.
(7. Enjoy!""",
                """Calories 280
Fat 8g
Carbs 30g
Fiber 5g
Sugar 4g
Protein 24g"""
            ),
            (13,
                "Unavailable",
                "One Bowl Chocolate Chip Banana Bread",
                "https://tasty.co/recipe/one-bowl-chocolate-chip-banana-bread",
                "banana|butter|sugar|egg|vanilla extract|baking soda|salt|flour|chocolate",
                """for 6 servings

3 ripe bananas
⅓ cup butter, melted
½ cup sugar
1 egg, beaten
1 teaspoon vanilla extract
1 teaspoon baking soda
salt, to taste
1 ½ cups all-purpose flour
½ cup mini chocolate chips""",
                "Over an hour",
                "No",
                "No",
                "No",
                "Yes",
                "Yes",
                "Yes",
                """(1. Preheat oven to 350˚F (180˚C).
(2. In a bowl, add the bananas and mash until smooth. Add in the melted butter and stir until well combined.
(3. Add the sugar, egg, vanilla, baking soda, salt, and flour, and stir until the batter is smooth.
(4. Add in the chocolate chips and pour the batter into a greased loaf pan. Top with additional chocolate chips.
(5. Bake for 50 minutes to an hour, or until a toothpick comes out clean.
(6. Cool completely before serving.
(7. Enjoy!""",
                """Unavailable"""
            ),
            (14,
                "Unavailable",
                "Pizza Bread Bowl",
                "https://tasty.co/recipe/pizza-bread-bowl",
                "bread boule|marinara sauce|mozzarella cheese|pepperoni|onion|basil|sausage|green bell pepper|white cheddar cheese",
                """for 6 slices

1 bread boule
1 cup marinara sauce
8 oz fresh mozzarella cheese
6 oz pepperoni
½ onion, sliced
½ cup fresh basil
1 cup sausage, cooked
1 green bell pepper, sliced
1 cup white cheddar cheese, shredded""",
                "Over an hour",
                "No",
                "Yes",
                "No",
                "Yes",
                "Yes",
                "No",
                """(1. Slice the top of the bread boule off and remove the insides.
(2. Spread ½ cup (130 G) of the marinara on the bottom of the boule, then layer with half of the mozzarella, 5 ounces (140 G) of the pepperoni, onions, basil, sausage, peppers, the other ½ cup (130 G) of marinara, the remaining mozzarella, and half of the white cheddar, and place the cap of the bread boule on top.
(3. Wrap the bread bowl in foil, then press with a heavy object for 30 minutes.
(4. Preheat oven to 350°F (175˚C).
(5. Remove the foil and sprinkle the remaining cheddar and pepperoni on top. Bake for 30 minutes, until cheese is golden brown.
(6. Cool for 10 minutes and slice.
(7. Enjoy!""",
                """Calories 608
Fat 38g
Carbs 32g
Fiber 2g
Sugar 4g
Protein 31g"""
            ),
            (15,
                "Sylvia Fountaine",
                "Vegan Shepherds Pie",
                "https://www.feastingathome.com/vegan-shepherds-pie-html/",
                "yukon potato|olive oil|vegan sour cream|turffle oil|garlic poweder|salt|pepper|nutritional yeast|vegan butter|onion|mushroom|celery|carrot|parsnip|peas|white beans|garlic|cracked pepper|thyme|water|apple cidar vinegar|white wine|flour|veggies stock|parsley|dijon mustard",
                """Mashed Potato Topping:
3 pounds yukon gold potatoes, unpeeled (or russets, peeled), quartered or diced.
4 tablespoons olive oil, or vegan butter
1/2 cup vegan sour cream ( like Kite Hill Sour cream)
1 tablespoon truffle oil (optional but amazing)
2 teaspoons granulated garlic powder
1 teaspoon salt
1/2 teaspoon pepper
1/2–1 teaspoon nutritional yeast– optional!

Filling
3 tablespoons olive oil or vegan butter
1 large onion, diced (or sub 2 cups leeks)
1 lb sliced mushrooms (cremini, button, shiitake, portobello, chanterelles or a mix)
1 1/2 cups celery, diced (or sub part or all fennel bulb)
1 1/2 cups carrots, peeled, diced in small 1/2 inch cubes
1 1/2 cups parsnips, peeled, diced in small 1/2 inch cubes
1 1/2 cup frozen peas
1 1/2 cups cooked white beans (or sub cubes of roasted sunchokes, cannellini beans, lentils, browned vegan “ground meat”, or seitan, etc.
6 cloves garlic- rough chopped
1 tsp salt, more to taste
1/2 tsp cracked pepper
1 tablespoon fresh thyme leaves ( or 1 teaspoon dried)
1/2 cup dry white wine (or sub water plus 1/2 teaspoon Apple Cider vinegar)
4 tablespoons flour ( or use GF flour)
3 cups rich veggie stock, (see notes) warmed, mixed with 2 teaspoon miso paste
1 teaspoon dijon mustard
1/2 cup fresh Italian Parsley, chopped""",
                "1 Hour 50 Mins",
                "Yes",
                "No",
                "No",
                "No",
                "Yes",
                "No",
                """(1. Preheat oven to 375
(2. Start with the mashed potatoes. Cut yukon gold potatoes, into halves or quarters. Make sure the pieces are similar in size. Place in a large pot, cover with an inch of water with 1 tablespoon kosher salt and simmer until knife tender about 20-25 minutes. Drain, saving 1 cup of potato water. 
(3. Make the stew: In a very large heavy bottom pot, heat oil over med heat.  Saute onions and mushrooms for 7-8 minutes (see notes), until fragrant, then add parsnips, carrots, celery, garlic, thyme, salt and pepper stirring for 1o mins until carrots are al dente and mushrooms give off their liquid. Cook off the liquid.
(4. Deglaze with 1/2 cup wine, scraping up any brown bits.  Let simmer on med-low until carrots/parsnips are perfectly tender and wine has cooked off. Add the peas and white beans.
(5. Sprinkle the veggies with 4 tablespoons flour ( or use GF flour) and stir it for about 2 minutes letting the flour cook a bit.
(6. Add 1 cup warm veggie broth to the pot, stirring until the stew thickens, then stir in the remaining broth a cup at a time, simmering, and letting it thicken.
(7. Add the mustard.  Turn off heat.
(8. Taste for salt, and add more to taste, and more cracked pepper if you like too. Add a few drops of apple cider vinegar to brighten, tasting as you add. Stir in the fresh parsley.
(9. Finish the Potatoes: Place the drained potatoes back into the potato pot. Mash with a potato masher and add olive oil, vegan sour cream,  granulated roasted garlic, salt, pepper and optional truffle oil and nutritional yeast.  Add a 1/4 cup- 1/2 cup of the hot potato water to loosen them ( easier to spread).Whip them up until creamy with the masher! Taste and adjust salt and pepper.
(10. Assemble:  Scoop the filling into a greased, large 9×13 inch baking dish, or a large oven-proof cast iron skillet or dutch oven, or smaller individual-sized baking dishes, or ramekins. ***At this point you could divide your stew mixture – adding cooked chicken, lamb or beef to part of it for meat-eaters. (For example, I like my shepherd’s pie, without meat. My husband likes his with meat, so I divide it, adding cooked lamb to his portion. When having guests over, you could do half and half if you like.)
(11. Spoon the creamy mashed potatoes over the stew, or use a piping bag and pipe out the potatoes over the stew. If potatoes seem too dry to pipe, whip in a little more hot potato water to them and they will loosen up nicely. Drizzle the top with a little truffle oil.
(12. Bake: Place baking dish or individual pies on a sheet-pan to catch the drippings, in a preheated 375F oven and bake until bubbly and golden, about 20-30 minutes.
(13. Garnish with Fresh parsley or a sprig of thyme.
NOTES
The filling can be made ahead and refrigerated (let it come to room temp before baking) and then assemble the shepherd pie before baking. I find making the potatoes the same day makes for lighter fluffier potatoes, but if in a pinch, assemble the whole thing ahead and refrigerate. Let come to room temp before baking.

Veggie Stock: I use 3 cups water plus 3 teaspoons of veggie bouillon paste, heat this up, and stir in the miso paste. This gives the stew a flavorful base.

Mushrooms: To elevate this dish, pan-sear the mushrooms in olive oil FIRST, season lightly with salt and pepper, cooking until they release all their liquid and let them caramelize a bit. Set them aside while you saute the onions and veggies, then add them back in with the wine.

The original recipe call for sunchokes - which add great flavor here, but can be hard to find. ( So I subbed white beans) If using sunchokes, wash well, no need to peel, cut into a medium dice and roast with a little olive oil salt and pepper in a 400F oven until a little crispy, first for the BEST flavor. Then add to the stew with the peas.""",
                """"Serving Size: -with White beans and Truffle oil:
Calories: 288
Fat: 13.1g
Sodium: 745.1mg
Sugar: 7.9g
Carbs: 36.1g
Fiber: 8.1g
Protein: 8.4g"""
            ),
            (16,
                "Erin C David",
                "Couscous with Olives and Sun-Dried Tomato",
                "https://www.allrecipes.com/recipe/232210/couscous-with-olives-and-sun-dried-tomato/",
                "vegetable broth|water|pear couscous|salt|black pepper|olive oil|pine nutes|garlic|shallot|black olives|sun-dried tomatoes|parsley",
                """1 ¼ cups vegetable broth
1 ¼ cups water
2 cups pearl (Israeli) couscous
1 pinch salt
1 pinch ground black pepper
5 tablespoons olive oil, divided
½ cup pine nuts
4 cloves garlic, minced
1 shallot, minced
½ cup sliced black olives
⅓ cup sun-dried tomatoes packed in oil, drained and chopped
1 cup vegetable broth
¼ cup chopped fresh flat-leaf parsley""",
                "50 Minutes",
                "Yes",
                "No",
                "No",
                "No",
                "No",
                "No",
                """(1. Bring 1 1/4 cup vegetable broth and water to a boil in a saucepan, stir in couscous, and mix in salt and black pepper. Reduce heat to low and simmer until liquid is absorbed, about 8 minutes.
(2. Heat 3 tablespoons olive oil in a skillet over medium-high heat; stir in pine nuts and cook, stirring frequently, until pine nuts smell toasted and are golden brown, about 1 minute. Remove from heat.
(3. Heat remaining 2 tablespoons olive oil in a saucepan; cook and stir garlic and shallot in the hot oil until softened, about 2 minutes. Stir black olives and sun-dried tomatoes into garlic mixture and cook until heated through, 2 to 3 minutes, stirring often. Slowly pour in 1 cup vegetable broth and bring mixture to a boil. Reduce heat to low and simmer until sauce has reduced, 8 to 10 minutes.
(4. Transfer couscous to a large serving bowl, mix with sauce, and serve topped with parsley and pine nuts.""",
                """Calories 528
Fat 29g
Sodium 455mg
Carbs 56g
Fiber 5g
Sugars 3g
Protein 13g"""
            ),
            (17,
                "isachandra",
                "Ultimate Tofu Breakfast Burrito Bowls",
                "https://www.allrecipes.com/recipe/256021/ultimate-tofu-breakfast-burrito-bowls/",
                "olive oil|tofu|salt|black pepper|onion powder|garlic powder|ground tumeric|lemon juice|jalapeno pepper|garlic|tomato|cumin|black bean|hash brown potato|avocado|hot sauce",
                """3 tablespoons olive oil, divided
1 (14 ounce) package extra-firm tofu, drained
½ teaspoon salt
black pepper to taste
1 ½ teaspoons onion powder
1 ½ teaspoons garlic powder
½ teaspoon ground turmeric
1 tablespoon fresh lemon juice
1 tablespoon olive oil
1 cup finely diced red onion
2 jalapeno peppers, seeded and chopped
½ teaspoon salt
3 cloves garlic, minced
2 cups chopped tomatoes
1 ½ teaspoons cumin
¼ cup chopped fresh cilantro
1 tablespoon fresh lemon juice
1 (15.5 ounce) can no-salt-added black beans, drained and rinsed
1 ½ cups cooked hash brown potatoes
1 avocado - peeled, pitted and sliced
1 teaspoon fresh lemon juice
¼ cup chopped fresh cilantro
1 teaspoon hot sauce, or to taste""",
                "45 minutes",
                "Yes",
                "No",
                "No",
                "No",
                "No",
                "No",
                """(1. Preheat a large, heavy skillet over medium-high heat. Add 2 tablespoons oil. Break tofu apart over skillet into bite-size pieces, sprinkle with salt and pepper, then cook, stirring frequently with a thin metal spatula, until liquid cooks out and tofu browns, about 10 minutes. (If you notice liquid collecting in pan, increase heat to evaporate water.) Be sure to get under the tofu when you stir, scraping the bottom of the pan where the good, crispy stuff is and keeping it from sticking.
(2. Add onion and garlic powders, turmeric, juice, and remaining tablespoon oil and toss to coat. Cook 5 minutes more.
(3. Preheat a heavy-bottomed saucepan over medium-high heat. Add oil. Cook onion and jalapenos with a pinch of salt, stirring, until translucent, about 5 minutes, Add garlic and cook, stirring, until fragrant, about 30 seconds. Add tomatoes, cumin, and remaining salt, and cook, stirring, until tomatoes become saucy, about 5 minutes. Add cilantro and lemon juice. Let cilantro wilt in. Add beans and heat through, stirring occasionally, about 2 minutes. Taste for salt and seasoning.
(4. Spoon some hash browns into each bowl, followed by a scoop of beans and a scoop of scramble. Top with avocado, a squeeze of fresh lemon juice, and a sprinkle of cilantro. Serve with hot sauce.""",
                """Calories 579
Fat 40g
Sodium 1171mg
Carbs 57g
Fiber 16g
Sugars 9g
Protein 22g"""
            ),
            (18,
                "veggigodess",
                "Ginger Veggie Stir-Fry",
                "https://www.allrecipes.com/recipe/24712/ginger-veggie-stir-fry/",
                "vegetable oil|ginger root|garlic|cornstarch|broccoli|snow pea|green bean|water|soy sauce|onion|salt",
                """4 tablespoons vegetable oil, divided
2 teaspoons chopped fresh ginger root, divided
1 ½ cloves garlic, crushed
1 tablespoon cornstarch
1 small head broccoli, cut into florets
¾ cup julienned carrots
½ cup snow peas
½ cup halved green beans
2 ½ tablespoons water
2 tablespoons soy sauce
¼ cup chopped onion
½ tablespoon salt""",
                "40 mins",
                "Yes",
                "No",
                "No",
                "No",
                "No",
                "No",
                """(1. Gather all ingredients.

(2. Place 2 tablespoons vegetable oil, 1 teaspoon ginger, garlic, and cornstarch in a large bowl; mix until cornstarch is dissolved.

(3. Add broccoli, carrots, snow peas, and green beans; toss lightly to coat.

(4. Heat remaining 2 tablespoons vegetable oil in a large skillet or wok over medium heat. Add vegetable mixture and cook for 2 minutes, stirring constantly to prevent burning.

(5. Stir in water and soy sauce; add onion, salt, and remaining 1 teaspoon ginger. Cook and stir until vegetables are tender but crisp.

(6. Serve hot and enjoy!""",
                """Calories 119
Fat 9g
Sodium 903mg
Carbs 8g
Fiber 2g
Sugars 3g
Protein 2g"""
            ),
            (19,
                "Rita",
                "Easy Vegan Pasta with Kale and Chickpeas",
                "https://www.allrecipes.com/recipe/260579/easy-vegan-pasta-with-kale-and-chickpeas/",
                "spaghetti|olive oil|garlic|kale|nutritional yeast|chickpeas|salt|black pepper",
                """1 (16 ounce) package spaghetti
¼ cup olive oil
5 cloves garlic, minced
1 bunch kale, chopped
2 tablespoons nutritional yeast
1 (15 ounce) can chickpeas
salt and freshly ground black pepper""",
                "22 mins",
                "Yes",
                "No",
                "No",
                "No",
                "Yes",
                "No",
                """(1. Bring a large pot of lightly salted water to a boil. Cook spaghetti in the boiling water, stirring occasionally, until tender yet firm to the bite, about 12 minutes. Drain, reserving about 1 cup of cooking water.
(2. Heat olive oil in a large skillet over medium heat and cook garlic until fragrant, about 1 minute. Add kale and cook, stirring constantly, until wilted, about 3 minutes.
(3. Stir cooked spaghetti into the skillet. Add nutritional yeast. Add enough of the reserved cooking water to create a thick sauce. Stir well. Add chickpeas and heat until warmed, 2 to 4 minutes. Season with salt and pepper.""",
                """Calories 692
Fat 17g
Sodium 305mg
Carbs 113g
Fiber 10g
Sugar 3g
Protein 24g"""
            ),
            (20,
                "Alvin Zhou",
                "Cookies & Cream Truffles",
                "https://tasty.co/recipe/cookies-cream-truffles-easy-dessert",
                "chocolate sandwhich cookie|cream cheese|white chocolate ",
                """
36 chocolate sandwich cookies
8 oz cream cheese, softened
12 oz white chocolate, melted""",
                "Unavailible",
                "No",
                "No",
                "No",
                "Yes",
                "Yes",
                "Likely",
                """(1. In a food processor, finely crush the cookies, reserving about 2 tablespoons of the mixture for sprinkling on top of the truffles.
(2. In a large bowl, combine the cookie crumbs and cream cheese, stirring until evenly mixed. Chill the mixture for about an hour or until it can be rolled into a ball and hold its shape.
(3. Divide and roll the mixture into golf ball-sized balls. Dip the truffles in the melted white chocolate and place on a baking sheet lined with parchment paper. Sprinkle the reserved cookie crumbs on top of the truffles before the chocolate hardens.
(4. Enjoy!""",
                """Calories 475
Fat 32g
Carbs 45g
Fiber 0g
Sugar 40g
Protein 7g"""
            )]



cursor.executemany("""INSERT INTO recipes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",recipies)

#cursor.execute("""INSERTMANY INTO recipes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
#               (,
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