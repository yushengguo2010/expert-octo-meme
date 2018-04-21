from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from SQLAlchemy.connet import engine, Base, User


# 创建表对应的类

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username= Column(String(20),nullable=False)
    password = Column(String(50))
    email = Column(String(20))
    def __repr__(self):
        return '<User(id="%s",username="%s",password="%s",email="%s")>'%(self.id,
                                                                         self.username,
                                                                         self.password,
                                                                         self.email)

Base.metadata.create_all()

Session = sessionmaker(engine)
session = Session()


def add_user():
	taka = User(username='taka', password='11222', email='xx@qq.com')
	budong = User(username='budong', password='555', email='kk@qq.com')
	session.add(taka)
	session.add(budong)
	ls = [User(username='which', password='qwe123',
			   email='dakl@163.com'),
		  User(username='rose', password='478956',
			   email='rose123@126.com')]
	session.add_all(ls)
	session.commit()


# add_user()

def search_user():
	# rs = session.query(User).all()
	rs = session.query(User).filter(User.username.like('ta%')).all()
	print(rs)


search_user()

def update():
	user = session.query(User).filter_by(username='which_wula').first()
	user.username = 'which'
	session.commit()
	print(user)


# update()

def delete_user():
	rs = session.query(User).filter_by(username='budong')[1]
	session.delete(rs)
	session.commit()


# delete_user()