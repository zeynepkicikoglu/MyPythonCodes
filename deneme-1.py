result= ("  hello world  ").count("l")
print(result)

result= ("  hello world  ").upper()
print(result)

result= ("  hello world  ").strip()
print(result)

result= ("  hello world  ").title()
print(result)

result= ("  hello world  ").strip().capitalize()
print(result)

sentence= ("www.hayirdirulan.com").count('a' ,0,6)
print(sentence)

sentence= (" www.hayirdirulan.com").startswith(" ")
print(sentence)

sentence= ("www.hayirdirulan.com").endswith("ü")
print(sentence)

list= ("bmw,mercedes,honda,opel").split()
print(list) 

student= ["zeynep" , "kıcıkoğlu" , [30,32,33]] 
com=f"{student[0]} {student[1]}'nun not ortalaması {(student[2][0] + student[2][1] + student[2][2])/3} dir."
print(com)

