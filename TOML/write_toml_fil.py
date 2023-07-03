#############################################################################################
#
#
#   https://pypi.org/project/toml/
#
#
#
#
#
#############################################################################################

import toml

data = {
  "target": {
    "ip": "xx.xx.xx.xx",
    "os": {
      "os": "win 10",
      "Arch": "x64"
    },
    "ports": {
      "ports": ["1", "2"],
      "1": {
        "service": "xxx",
        "ver": "5.9",
      }
    } 
  }
}

toml_string = toml.dumps(data)  # Output to a string

output_file_name = "output.toml"

with open(output_file_name, "w") as toml_file:
    toml.dump(data, toml_file)

print(data)


