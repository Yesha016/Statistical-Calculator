from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

Session = sessionmaker(bind=engine)
session = Session()

