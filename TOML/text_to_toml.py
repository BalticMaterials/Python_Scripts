import tomllib
  
txt = """
  
title = "GeeksforGeeks TOML"
  
[tutorials]
info = "Different Tutorials Available"
subjects = ["OS","DBMS","DSA","Cloud Computing"]
  
    [tutorials.OS]
    chapters = ["Deadlocks","CPU Scheduling","Process","Threading"]
  
    [DSA]
    linear = ["Stack","Queue","Linked List"]
  
    non_linear = ["Graph","Tree"]
[modern_tech]
  
subjects = ["AI","ML","DL"]
  
  
"""
  
toml_d = tomllib.loads(txt)
  
print(toml_d)