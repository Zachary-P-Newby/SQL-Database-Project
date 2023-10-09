from proto_functions_one import *

table = input("Enter table: ")
column = input("Enter Column: ")
attribute = input("Enter attribute: ")

results = search_column_by_attribute(table, column, attribute)

display_results(results)

