import tomllib

strings = """
# Das ist ein TOML Beispiel

name = "TOML Example"

[author]
name = "Tjark Ziehm"
birthday = 1998-05-06T00:00:00-08:00

[artikels]

[artikels.drafts]
liste = ["Was ist TOML?"]

[artikels.published]
liste = ["Was ist Python?"]
"""

data = tomllib.loads(strings)

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
    
import tomli_w as tomlwriter

docs = {
    "author": {
        "name": "Felix",
        "age": 24
    }
}

print(tomlwriter.dumps(docs))

# [author]
# name = "Felix"
# age = 24
