class Person(object):
	name = None
	identity = None
	ptype = None
	bloodg = None
	dept = None

	def __init__(self, name, identity, ptype, dept, bloodg=None):
		self.name = name
		self.identity = identity
		self.ptype = ptype
		self.dept = dept
		self.bloodg = bloodg
