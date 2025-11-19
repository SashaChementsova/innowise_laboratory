from datetime import datetime

# Define a Function for the Profile and Calculations

def generate_profile(age):
    if 0 <= age <= 12:
        return "child"
    elif 13 <= age <= 19:
        return "teenager"
    elif age >= 20:
        return "adult"
    return "not defined"

# Get User's Info

user_name = input("Hi! Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = datetime.now().year - birth_year

# Gather Hobbies

hobbies = []
while 1:
    hobby = input("Enter your favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

# Process and Generate the Profile

life_stage = generate_profile(current_age)
user_profile = {
    "Name": user_name,
    "Age": current_age,
    "Life Stage": life_stage,
    "Hobbies": hobbies
}

# Display User's Info

text = f"---\nProfile Summary:\n"
for key, value in user_profile.items():
    if key == "Hobbies":
        if len(value) == 0:
            text += f"You didn't mention any hobbies.\n"
        else:
            text += f"Favorite Hobbies ({len(value)}):\n"
            for i in value:
                text += f"- {i}\n"
    else:
        text += f"{key}: {value}\n"
text += f"---"
print(text)

