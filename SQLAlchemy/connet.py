# 连接数据库
from sqlalchemy import create_engine
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'infodb'
USERNAME = 'root'
PASSWORD = 'q1325066'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,
                                                              PASSWORD,
                                                              HOSTNAME,
                                                              PORT,
                                                              DATABASE)

engine = create_engine(DB_URI)

# 测试是否连接sqlalchemy
with engine.connect() as con:
    rs = con.execute('SELECT 1')

#声明映像
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
session = Session()
