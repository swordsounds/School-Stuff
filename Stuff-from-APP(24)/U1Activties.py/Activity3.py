# 1) Print the full dictionary
# 2) Add an additional country to the dictionary (Should now be 11) and print
# out what country you added by referencing the dictionary (Do not type
# it in as a string)
# 3) Delete the first entry in your dictionary
# 4) Print the full dictionary again
# 5) Use the pop() method to delete the second item in your dictionary
# 6) Print the full dictionary again

#Canada CAN
# Afghanistan	AFG	
# Albania		ALB	
# Algeria		DZA	
# American Samoa	ASM	
# Andorra	AND	
# Angola	GO	
# Anguilla	AIA	
# Antarctica	ATA	
# Barbuda	ATG	
# Argentina		ARG	
# Armenia		ARM	

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

full_dict.popitem()

print(full_dict)
