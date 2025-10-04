def get_name_parts(full_name):# John Kato
  parts=full_name.split()# ['John','Kato']
  first_name=parts[0] #John
  last_name=parts[-1] #Kato
  return first_name,last_name #("John","Kato")
fname,lname=get_name_parts("John Kato") #fname,lname=("John","Kato")
print(f"First Name: {fname}")
print(f"Last Name: {lname}")
