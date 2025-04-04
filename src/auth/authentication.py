import bcrypt
import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
#load_dotenv()

# Database setup with PostgreSQL
DATABASE_URL ="postgresql://postgres:zFlVCAwiPhjleNqAlIkQlhcXUgoztkyU@metro.proxy.rlwy.net:15223/railway"      # os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables")

logger.info(f"Connecting to database... {DATABASE_URL.split('@')[1]}")  # Log URL without credentials

try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
        echo=True  # Enable SQL logging
    )
    # Test connection
    with engine.connect() as conn:
        logger.info("Database connection successful!")
except Exception as e:
    logger.error(f"Database connection failed: {str(e)}")
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "service_users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(255))  # Now stores plain password
    company = Column(String(100))
    role = Column(String(20))

Base.metadata.create_all(bind=engine)

def get_password_hash(password: str) -> str:
    """Hash a password for storing."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a stored password against one provided by user"""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def login(username: str, password: str) -> bool:
    """Simple password matching."""
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if user and user.password_hash == password:  # Direct string comparison
            st.session_state['user'] = {
                'id': user.id,
                'username': user.username,
                'company': user.company,
                'role': user.role
            }
            return True
        return False
    finally:
        db.close()

def logout():
    """Clear the user session."""
    if 'user' in st.session_state:
        del st.session_state['user']

def is_authenticated() -> bool:
    """Check if a user is currently authenticated."""
    return 'user' in st.session_state

def get_current_user() -> Optional[dict]:
    """Get the current authenticated user's information."""
    return st.session_state.get('user')

def register(username: str, password: str, company: str, role: str = 'user') -> tuple[bool, str]:
    """Register a new user.
    Returns: (success: bool, message: str)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
        
    db = SessionLocal()
    try:
        if db.query(User).filter(User.username == username).first():
            return False, "Username already exists"
        
        password_hash = get_password_hash(password)
        new_user = User(
            username=username,
            password_hash=password_hash,
            company=company,
            role=role
        )
        db.add(new_user)
        db.commit()
        return True, "Registration successful! You can now login."
    except Exception as e:
        db.rollback()
        logger.error(f"Registration error: {str(e)}")
        return False, "Registration failed. Please try again."
    finally:
        db.close()

# Add this new function after the existing functions
def update_password_hash(username: str) -> bool:
    """Update plain password to hashed password for existing user."""
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if user:
            # Hash the existing plain password
            plain_password = user.password_hash  # Current plain password
            hashed_password = get_password_hash(plain_password)
            user.password_hash = hashed_password
            db.commit()
            logger.info(f"Password hash updated for user: {username}")
            return True
        return False
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to update password hash: {str(e)}")
        return False
    finally:
        db.close()
