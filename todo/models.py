# in models.py
from datetime import datetime
import secrets
import pandas

# initializedb.py
from sqlalchemy import engine_from_config
from todo import SQLALCHEMY_URL

from sqlalchemy import (
    Column, Unicode, Integer, DateTime, Boolean, relationship
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#เพิ่ม python เข้าไปบรรทัดนึงให้คอนเนคดาต้าเบส (resource) เข้ามาโดย
data = pd.read_csv('User.csv')

class LastLogin
    """DateTime of each user's last_login"""
    now = Column(DateTime)
    havent_login_for_a_week = Column(Boolean, default=True)

#class Task(Base):
    #"""Tasks for the To Do list."""
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    note = Column(Unicode)
    #creation_date = Column(DateTime, nullable=False)
    #due_date = Column(DateTime)
    #completed = Column(Boolean, default=False)
    #user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    #user = relationship("user", back_populates="tasks")

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()

class User(Base):
    """The User object that owns tasks."""
    id = Column(Integer, primary_key=True)
    username = Column(Unicode, nullable=False)
    #email = Column(Unicode, nullable=False)
    #password = Column(Unicode, nullable=False)
    #date_joined = Column(DateTime, nullable=False)
    #token = Column(Unicode, nullable=False)
    #tasks = relationship("Task", back_populates="user")
    tag = Column(Integer)

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.date_joined = datetime.now()
        self.token = secrets.token_urlsafe(64)

    def main():
    settings = {'sqlalchemy.url': SQLALCHEMY_URL}
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    if bool(os.environ.get('DEBUG', '')):
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

#models.py

class Login(Base):
    userid = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    note = Column(Unicode)
    now = Column(DateTime)
    havent_login_for_a_week = Column(Boolean, default=True)

In myapp/management/commands/populate.py:

class Command(BaseCommand):

def handle(self, *args, **options):

    # Open ModelConnection
    from django.conf import settings
    database_name = settings.DATABASES['default']['NAME']
    database_url = 'sqlite:///{}'.format(database_name)
    engine = create_engine(database_url, echo=False)

    # Insert data data
    agencies = pd.DataFrame({"name": ["Agency 1", "Agency 2", "Agency 3"]})
    agencies.to_sql("agency", con=engine, if_exists="replace")