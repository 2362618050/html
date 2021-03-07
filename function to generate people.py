import names
def generate_people_Data(num_people = 0,num_male= 0,num_female= 0):
    '''When the male parameter and female parameter are both 0, the name list without gender classification is output,'''
    # print(num_people)
    if num_people is not None and num_male ==0 and num_male ==0:

        return [names.get_full_name() for i in range(num_people)]
    else:

        last = [[names.get_full_name(gender='male') for i in range(num_male)],
        [names.get_full_name(gender='female') for i in range(num_female)]]
    return last

a = generate_people_Data(num_people=5,num_male=0,num_female=0)
print(a)
# print(names.get_full_name(gender='male'))