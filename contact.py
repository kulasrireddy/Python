# Create an empty dictionary to store contacts 
contacts = {} 
contacts["Pramod"] = "98765-43210" 
contacts["Sagar"] = "87654-32109" 
contacts["Tenneti"] = "76543-21098" 
print("Contacts after adding:")
print(contacts) 
contacts["Sagar"] = "99999-88888" 
print("\nContacts after updating Sagar's number:") 
print(contacts) 
del contacts["Tenneti"] 
print("\nContacts after deleting Tenneti:")
print(contacts) 
print("\nPhone number for Pramod:") 
print(contacts["Pramod"]) 

 

 

 