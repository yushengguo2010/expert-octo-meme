from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relation

from SQLAlchemy.connet import Base


class Department(Base):
	__tablename__ = 'department'
	d_id = Column(Integer, primary_key=True, autoincrement=True)
	d_name = Column(String(50))
	student = relation('Student', backref='department')

	def __repr__(self):
		return '<Department(d_id="%s",d_name="%s")>' % (self.d_id,
														self.d_name)


class Student(Base):
	__tablename__ = 'student'
	s_id = Column(Integer, primary_key=True)
	s_name = Column(String(20))
	d_id = Column(Integer, ForeignKey('department.d_id'))
	stu_details = relation('Stu_details', uselist=False)

	def __repr__(self):
		return '<Student(s_id="%s",s_name="%s",d_id="%s")>' % (self.s_id,
															   self.s_name,
															   self.d_id)


class Stu_details(Base):
	__tablename__ = 'stu_details'
	id = Column(Integer, primary_key=True)
	age = Column(Integer)
	city = Column(String(100))
	s_id = Column(Integer, ForeignKey('student.s_id'), unique=True)
	student = relation('Student')


Base.metadata.create_all()
