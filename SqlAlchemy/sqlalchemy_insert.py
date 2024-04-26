# from typing import List
# from typing import Optional
# from sqlalchemy import ForeignKey
# from sqlalchemy import String
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from sqlalchemy import select

# class Base(DeclarativeBase):
#   pass

# class City(Base):
#   __tablename__ = "cities"

#   id: Mapped[int] = mapped_column(primary_key=True)
#   name: Mapped[str] = mapped_column(String(250))
#   population: Mapped[int]

#   def __repr__(self) -> str:
#     return f"City(id={self.id!r}, name={self.name!r}, population={self.population!r}"

# if __name__=="__main__":
#   # create table
#   engine = create_engine("sqlite:///tutorial.db", echo=True)
#   Base.metadata.create_all(engine)

#   # insert rows
#   with Session(engine) as session:
#     hanoi = City(
#       name="Ha Noi",
#       population=1000000
#     )
#     hcm = City(
#       name="TP Ho Chi Minh",
#       population=2000000
#     )
#     da_nang = City(
#       name="Da Nang",
#       population=3000000
#     )

#     session.add_all([hanoi, hcm, da_nang])
#     session.commit()

#   # simple select
#   session = Session(engine)
#   stmt = select(City)

#   for user in session.scalars(stmt):
#     print(user)
