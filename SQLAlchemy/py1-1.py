from datetime import datetime, date

from sqlalchemy import Column, Integer, String, Text, Boolean, Date, DateTime

from SQLAlchemy.connet import engine, Base


class Xuesheng(Base):
	__tablename__ = 'students'
	id = Column(Integer,primary_key=True,autoincrement=True)
	name = Column(String(20),nullable=False)
	gender = Column(Boolean)
	admission_time = Column(DateTime,default=datetime.now())
	birth_date = Column(Date)
	article = Column(Text)

Base.metadata.create_all()

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
session = Session()

s1 = Xuesheng(name='xiaoming',gender='True',birth_date=date(2016,10,12))
session.add(s1)
session.commit()