import sqlite3

def listAllRecipes():
    """
    Prints out all recipes with their id and basic info to the console
    """
    connection = sqlite3.connect("..\databases\\cookbook.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, author, source, totalTime, vegan FROM recipes")
    result = cursor.fetchall()
    
    print("  Number | Name | Author | Source | Total Prep Time | Is it Vegan\n")
    for item in result:
        print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]} | {item[5]}\n")
    connection.close()
    input("Press Enter to Continue")


def printRecipe(id = 1):
    """
    Prints out recipe by id to the console,
    Including name, author, url, ingrideients, total prep time, directions, and nutrition facts
    """
    connection = sqlite3.connect("..\databases\\cookbook.db")
    cursor = connection.cursor()

    cursor.execute(f"""SELECT name, author, source, ingredients, totalTime, directions, nutritionFacts FROM recipes WHERE id like '{id}'""")
    result = cursor.fetchone()
    print(f"{result[0]}\n----------\n")
    print(f"By {result[1]} - {result[2]}\n")
    print(f"Ingredients:\n{result[3]}\n")
    print(f"Total Time: {result[4]}\n")
    print(result[5] + "\n")
    print(f"Nutrition facts:\n{result[6]}")

    connection.close()
    input("Press Enter to Continue")

def listVeganRecipes():
    """
    Returns all vegan recipes and prints them to the console
    """
    connection = sqlite3.connect("..\databases\\cookbook.db")
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE vegan LIKE 'yes'")
    result = cursor.fetchall()
    connection.close()
    print("Index | Name | Author | Source | Total Prep Time\n")
    for item in result:
        print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")

    connection.close()
    input("Press Enter to Continue")

def listNonVeganRecipes():
    """
    Returns all non-vegan recipes and prints them to the console
    """
    connection = sqlite3.connect("..\databases\\cookbook.db")
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE vegan LIKE 'No'")
    result = cursor.fetchall()
    connection.close()
    print("Index | Name | Author | Source | Total Prep Time\n")
    for item in result:
        print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")

    connection.close()
    input("Press Enter to Continue")



def selectASubstance():
    """Select a substance for listAllWithSubstance() and listAllWithOutSubstance() and return that substance"""
    substances = {"meat","fish","dairy","wheat","egg"}
    print("")
    choice = input("Enter a substance - meat, fish, dairy, wheat, or egg: (X to quit) ")
    choice = choice.lower()
    
    if choice == "x":
        print("Returning to main menu...\n")
    elif choice == "meat":
        return "meat"
    elif choice == "fish":
        return "fish"
    elif choice == "dairy":
        return "dairy"
    elif choice == "wheat":
        return "wheat"
    elif choice == "egg":
        return "egg"
    else:
        print("ERROR: Enter a valid choice")
        selectASubstance()

def listAllWithSubstance(substance = "wheat"):
    """
    Lists all recipes with the specified substance, ex. Wheat, Meat, Dairy, Fish
    """
    connection = sqlite3.connect("..\databases\\cookbook.db")
    cursor = connection.cursor()

    if substance == "meat":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE meat LIKE 'Yes'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")

    elif substance == "fish":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE fish LIKE 'Yes'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")
    
    elif substance == "dairy":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE dairy LIKE 'Yes'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")
    
    elif substance == "wheat":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE wheat LIKE 'Yes'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")
    
    elif substance == "egg":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE meat LIKE 'Yes'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")
    
    else:
        print("ERROR! VALUE INVALID")

    connection.close()

def listAllWithOutSubstance(substance = "wheat"):
    """
    Lists all recipes without the specified substance, ex. Wheat, Meat, Dairy, Fish
    """
    connection = sqlite3.connect("..\databases\\cookbook.db")
    cursor = connection.cursor()

    if substance == "meat":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE meat LIKE 'No'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")

    elif substance == "fish":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE fish LIKE 'No'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")
    
    elif substance == "dairy":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE dairy LIKE 'No'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")
    
    elif substance == "wheat":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE wheat LIKE 'No'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")
    
    elif substance == "egg":
        cursor.execute("SELECT id, name, author, source, totalTime FROM recipes WHERE meat LIKE 'No'")
        result = cursor.fetchall()
        connection.close()
        print("Index | Name | Author | Source | Total Prep Time\n")
        for item in result:
            print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
        input("Press Enter to Continue")
    
    else:
        print("ERROR! VALUE INVALID")

    connection.close()

def searchForIngredient():
    """
    Searches for and lists out all recipes containing the specified ingredient
    """
    print("")
    ingredient = input("Enter an ingredient: (X to quit) ")
    ingredient = ingredient.lower()

    if ingredient != "x":
        connection = sqlite3.connect("..\databases\\cookbook.db")
        cursor = connection.cursor()

        cursor.execute(f"SELECT id, name, author, source, totalTime FROM recipes WHERE searchIngredients LIKE '%{ingredient}%'")
        result = cursor.fetchall()
        connection.close()

        if result:
            print("")
            print("Index | Name | Author | Source | Total Prep Time\n")
            for item in result:
                print(f"* {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n")
            connection.close()
            input("Press Enter to Continue")
        else:
            print("Ingredient not found enter again")
            connection.close()
            searchForIngredient()


def searchForIndex():
    """Call printRecipe on recipe with matching index number"""
    print("")
    index = input("Enter recipe index: (X to quit) ")
    if index == "X" or index == "x":
        pass
    elif int(index) in range(1,21):
        printRecipe(int(index))
    else:
        print("Error! Enter an index number between 1 and 20 (inclusive)")
        searchForIndex()

