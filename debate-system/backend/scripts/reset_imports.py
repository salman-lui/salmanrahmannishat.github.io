from sqlalchemy import inspect, text

from web.backend.database.connection import engine
from web.backend.database.models import Base

tables_to_reset = ["file", "row", "question"]


def main():
    with engine.connect() as connection:
        with connection.begin():
            for table in tables_to_reset:
                connection.execute(text(f'DROP TABLE IF EXISTS "{table}" CASCADE'))
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
