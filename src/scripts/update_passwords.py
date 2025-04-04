from auth.authentication import SessionLocal, User, update_password_hash
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_all_passwords():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        for user in users:
            if update_password_hash(user.username):
                logger.info(f"Updated password for {user.username}")
            else:
                logger.error(f"Failed to update password for {user.username}")
    finally:
        db.close()

if __name__ == "__main__":
    update_all_passwords()