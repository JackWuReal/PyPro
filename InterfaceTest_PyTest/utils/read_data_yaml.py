import yaml

f = open("../config/data.yaml", "r", encoding="utf-8")
data = yaml.safe_load(f)
print(data["hero"])
print(data["hero_name"])
print(data["heros"])
print(data["hero_name_list"])

