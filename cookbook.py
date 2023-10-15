from functions import *

print("""
      
Welcome to Zach's digital cookbook!
We've got an assortment of 20 recipes including healthy vegan options.
Enter a number to select an option.
    """)

running = True

def selectOption():

    """Enter a number to select an option (1-8) to select an option"""
    print("""
    1. List all recipes
    2. Print recipe
    3. List all vegan recipes  
    4. List all non-vegan recipes
    5. List all recipes with a certain substance (ie. dairy)
    6. List all recipes without a certain substance (ie. dairy)
    7. Search for recipes containing a specific ingredient
    8. Quit
    """)
    choice = int(input("Enter a number between 1 and 8 to select an option: "))

    if choice == 1:
        listAllRecipes()
        return True
    
    elif choice == 2:
        searchForIndex()
        return True
    
    elif choice == 3:
        listVeganRecipes()
        return True
    
    elif choice == 4:
        listNonVeganRecipes()
        return True
    
    elif choice == 5:
        substance = selectASubstance()
        listAllWithSubstance(substance)
        return True
    
    elif choice == 6:
        substance = selectASubstance()
        listAllWithOutSubstance(substance)
        return True
    
    elif choice == 7:
        searchForIngredient()
    
    elif choice == 8:
        return False
    
    else:
        print("Error! Enter an index number between 1 and 8 (inclusive)")
        return True


    
while running:
    print(""*3)

    forward = selectOption()

    if forward == False:
        running = False

else:
    print("Goodbye!")