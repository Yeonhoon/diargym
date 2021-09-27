from passlib.context import CryptContext


# hashing password 만들기
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def produce_hash_password(password: str):
        return pwd_cxt.hash(password)

    # 입력된 패스워드와 hash처리된 패스워드 검증
    def verify_password(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
