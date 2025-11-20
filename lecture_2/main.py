user_name=input('Hello! What is your full name?')
birth_year_str=input('What is your birth year? honey?')
birth_year=int(birth_year_str)
print(user_name, birth_year)
current_age=2025-birth_year
hobbies=[]
def generate_profile(current_age):
    if 0<=current_age<=12:
        return ('Child')
    elif 13<=current_age<=19:
        return('Teenager')
    elif current_age>=20:
        return('Adult')
while True :
    hobby=input('Enter a favorite hobbie or type "stop"?')
    if hobby.lower()=='stop':
        print("it' ok")
        break
    if hobby:
        hobbies.append(hobby)

life_stage=generate_profile(current_age)
user_profile={'Name': user_name, "Age":current_age,"Life Stage": life_stage, 'Hobbies': hobbies}
info=f"""
Profile summary
Name: {user_profile['Name']}
Age: {user_profile['Age']}
Life stage: {user_profile['Life Stage']}
"""
print(info)
r=len(hobbies)
for i in range(r):
    print("Favorite hobbies"+hobbies.item(i))
