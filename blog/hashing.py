from passlib.context import CryptContext

# Creating Hash password
pwd_ctx = CryptContext(schemes=["bcrypt"])


class Hash:
    @staticmethod
    def bcrypt(password):
        return pwd_ctx.hash(password)

    @staticmethod
    def verify(database_pwd, request_pwd):
        return pwd_ctx.verify(request_pwd, database_pwd)
