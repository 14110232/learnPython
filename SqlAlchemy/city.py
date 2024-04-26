from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import insert
from sqlalchemy import select
import read_csv_module

class Base(DeclarativeBase):
  pass

class City(Base):
  __tablename__ = "cities"
  CSV_PATH = '../files/cities.csv'

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(250))
  population: Mapped[int]

  engine = create_engine("sqlite:///tutorial.db", echo=True)

  def __repr__(self) -> str:
    return f"City(id={self.id!r}, name={self.name!r}, population={self.population!r}"

  def create_table(self):
    Base.metadata.create_all(self.engine)

  def import_rows(self):
    new_rows = read_csv_module.read_csv(self.CSV_PATH)
    stmt = insert(City.__table__).values(
      [{'name': name, 'population': population} for name, population in new_rows[:-1]])

    with self.engine.connect() as conn:
      result = conn.execute(stmt)
      conn.commit()

  def show(self):
    session = Session(self.engine)
    stmt = select(City)
    for city in session.scalars(stmt):
      print(city)
