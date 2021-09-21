from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///:memory:', echo=True)
db_section = scoped_session(sessionmaker(autocommit=False, binds=engine))

Base = declarative_base()
Base.query = db.session.query_property()

# Tables 
class Developers(Base):
    __tablename__ = 'developers'
    id = Column(Integer, primary_keys=True)
    name = Column(String(30), index=True)
    old = Column(Integer)

    def __repr__(self):
        return f'Developer Name: {self.name}'
