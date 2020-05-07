# making a dictionary of a dictionary

# screening candidates based on certain constraints.

candidate_dict = {}
number_of_candidates = int(input("Enter the number of candidates : "))

for i in range(number_of_candidates):
    # creating a temporary dictionary to store all resume keywords
    temp_dict = {}
    print("Enter the following details : ")
    name = input("Name of Candidate : ")
    # taking in experience(in years), languages known, project_supervision experience
    experience = int(input("Years of Experience : "))
    languages = input("Languages Known(separated by a comma) : ").split(sep=',')
    project_supervision = bool(input("Project Supervision(True or False) : "))
    temp_dict['Experience'] = experience
    temp_dict['Languages'] = languages
    temp_dict['Project_Supervision'] = project_supervision
    candidate_dict[name] = temp_dict

# creating a list of candidate names who have passed the screening
passed = []

# constraints
min_experience = 4
required_languages = ['Python', 'Java']
for name, cv_dict in candidate_dict.items():
    if cv_dict['Experience'] >= min_experience and \
            (set(required_languages).issubset(set(cv_dict['Languages'])) or
             cv_dict['Project_Supervision'] == 'True'):
        passed.append(name)

print('The following candidates have cleared the first round')
print(*passed, sep="\n")
