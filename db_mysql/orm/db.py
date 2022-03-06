import os
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql://root:password@localhost/dev_data', echo=False)

Session = sessionmaker(bind=engine)
session = Session()
