from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:xd10101994@localhost/postgres")
Session = sessionmaker(bind=engine)
session = Session()
