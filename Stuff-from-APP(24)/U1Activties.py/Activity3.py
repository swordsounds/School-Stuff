full_dict = {"Afghanistan": "AFG", "Albania": "ALB", "Algeria": "DZA", 
             "American Samoa": "ASM", "Andorra": "AND", "Angola": "GO", 
             "Anguilla": "AIA", "Antarctica": "ATA", "Barbuda": "ATG", 
             "Argentina": "ARG"}
print(full_dict)

full_dict["Armenia"] = "ARM"

print(f"{list(full_dict)[-1]} has been added to the dictionary.")

print(full_dict)

full_dict.pop("Afghanistan")

print(full_dict)

full_dict.pop("Albania")

print(full_dict)

full_dict.popitem()

print(full_dict)