'''
1) Create a dictonary called student
keys = names
value = marks scored in 3 subs

2) find the name of the student who scored highest in maths
3) name of the student whose sum of 3 subjets is highest
'''
student = {'john':{'physics':95,'chemistry':93,'maths':98},'jane':{'physics':99,'chemistry':97,'maths':100},'charles':{'physics':99,'chemistry':99,'maths':99}}
math_highest = 0
total_highest = 0
math_topper = ''
class_topper = ''
for key in student:
    if student[key]['maths']>math_highest:
        math_highest = student[key]['maths']
        math_topper = key
    sum = student[key]['physics'] + student[key]['chemistry'] + student[key]['maths']
    if sum > total_highest:
        total_highest = sum
        class_topper = key
print('Highest score in maths: {}, scored by {}'.format(math_highest,math_topper))
print('Top score: {}, scored by {}'.format(total_highest,class_topper))