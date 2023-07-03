######################################################################################
#
#
#
#
#   https://www.geeksforgeeks.org/handling-toml-files-using-python/
#
#
######################################################################################


import tomllib  
  
# Opening a Toml file using tomlib

with open("test.toml","rb") as toml:
    toml_dict = tomllib.load(toml)
  
# Printing the entire fetched toml file
print(toml_dict)

# Fetching and printing particular value from toml file
print(toml_dict["servers"]["servers.alpha"])