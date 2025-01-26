from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLite database (you can change this to PostgreSQL, MySQL, etc.)
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base = declarative_base()

# Define a model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create the database tables
Base.metadata.create_all(engine)