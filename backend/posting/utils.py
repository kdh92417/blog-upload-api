import bcrypt

from posting.models import Posting


def hash_password(password: str):
    """
    bcrypt를 이용한 비밀번호 암호화
    :param password: string
    :return: 암호호된 비밀번호
    """
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    decode_password = hashed_password.decode("utf-8")
    return decode_password


def check_password(password: str, instance: Posting):
    """
    비밀번호 체크
    :param password: string
    :param instance: PostingSerializer
    :return: Boolean
    """
    encoded_password = password.encode("utf-8")
    encoded_db_password = instance.password.encode("utf-8")
    return bcrypt.checkpw(encoded_password, encoded_db_password)
