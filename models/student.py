from .person import Person

class Student(Person):
	year = None
	classname = None


	def __init__(self, year, classname, name, dept, ptype, identity, bloodg=None ):
		self.year = year
		self.classname = classname
		super(Student, self).__init__(name, identity, ptype, dept, bloodg)
		
	def __str__(self):
		return self.name

	def __repr__(self):
	 	return self.name + '; ' + self.identity
