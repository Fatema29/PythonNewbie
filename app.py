from datasets.stdataset import ST_DATASET
from models.teacher import Teacher
from models.student import Student

dataset = ST_DATASET

stlist = []
teacherlist = []

for data in dataset:
	# print(data, end='\n\n')
	# print(data['type'])
	# print(data.get('ptype', 123), end='\n\n')
	ptype = data['type']
	
	if ptype == 'student':
		# year, classname, name, dept, ptype, identity, bloodg
		student = Student(data['year'], data['classname'], data['name'], data['dept'], data['type'], data['id'], data['bloodg'])
		stlist.append(student)
	elif ptype == 'teacher':
		#name, identity, ptype, dept, designation, salary, bloodg
		teacher = Teacher(data['name'], data['id'], data['type'], data['dept'], data['designation'], data['salary'], data['bloodg'])
		teacherlist.append(teacher)

print(stlist, end='\n\n')
print(teacherlist)
