from passlib.context import CryptContext
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():

    def hashPassword(password):
        return pwd_context.hash(password)

    def verifyPassword(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

    def verify_password(plain_password: str, hashed_password: str):
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
