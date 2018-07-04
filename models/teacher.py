from .person import Person

class Teacher(Person):
	designation = None
	salary = None

	def __init__(self, name, identity, ptype, dept, designation, salary, bloodg=None):
		self.designation = designation
		self.salary = salary
		super(Teacher, self).__init__(name, identity, ptype, dept, bloodg)

	def __str__(self):
		return self.designation +'> ' + self.salary

	def __repr__(self):
		return self.designation +'> ' + self.salary