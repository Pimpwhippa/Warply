#models.py
class User(Base):
    """Tag 1-10 of each user"""
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    last_login = Column(DateTime, nullable=False)
    tag = Column(Unicode) #binary encoding?
    #tag1, 1st_digit is a column by itself??

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()