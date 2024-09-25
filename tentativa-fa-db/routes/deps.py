from db.connection import session

def get_conection():
    db_session = session()
    try:
         yield db_session
    finally:
        db_session.close()
