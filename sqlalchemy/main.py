from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg://%s:%s@%s:%s/%s' % ('oleg', 'postgres', 'storage', 5433, "sqlalchemy"))
    session: Session = Session(engine)

    print("Server started with SQLAlchemy ORM initialized")