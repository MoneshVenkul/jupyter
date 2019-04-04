# Lists

courses = ['python', 'iot', 'uit']
print(courses)
courses.sort()
print(courses)
print(len(courses))
print(courses[1])

courses[1]='ml'
print(courses)

courses.append('dm')
courses.insert(1, 'sqat')
print(courses)

courses.remove('sqat')
print(courses)

if 'ml' in courses:
    print('ml is part of courses')
else:
    print('no')

courses.clear()
print(courses)



#Tuples
tcourses = ('python', 'iot', 'uit')
print(tcourses)
'''
tcourses[1] = 'ml'
print(tcourses)
'''

#Sets
scourses = {'python', 'iot', 'uit'}
print(scourses)
print('python' in scourses)
print('python3.7' in scourses)

scourses.add('ml')
print(scourses)
scourses.update(['dw', 'dm', 'sqat'])
print(scourses)
scourses.remove('dw')
print(scourses)

#Dictionary
dcourses = {
    "python": "x",
    "iot": "y",
    "uit": "z"
}
print(dcourses)
print(dcourses["python"])
dcourses["python"] = "a"
print(dcourses)

for i in dcourses:
    print(i)

for j in dcourses.values():
    print(j)

for (i, j) in dcourses.items():
    print(i, j)
