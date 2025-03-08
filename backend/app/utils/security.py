from datetime import UTC, datetime, timedelta
from typing import Union

import jwt
from argon2 import PasswordHasher
from app.core.config import variables

# Setting up the argon2ID with owasp defined guidelines https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
ph = PasswordHasher(parallelism=1, memory_cost=19, hash_len=16)
ACCESS_TOKEN_EXPIRE_MINUTES = 240


def hash_password(password: str) -> str:
    """
    hashes a plain-text password and returns it.

    A hashing function that utilizes the Argon2ID hashing algorithm and
    incorporates the suggestions from the OWASP cheatsheet for storing
    passwords, for e.g.:
        -> Degree Of Parallelism = 1
        -> Memory Cost = 19 MiB

    Args:
        password: The password to be hashed.

    Returns:
        a hashed password of length 73.
    """
    result = ph.hash(password=password)

    return result


def verify_password(password: str, hash: str) -> bool:
    """[TODO:summary]

    [TODO:description]

    Args:
        password: [TODO:description]
        hash: [TODO:description]

    Returns:
        [TODO:description]
    """
    return ph.verify(hash=hash, password=password)


def create_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expires_on = datetime.now(UTC) + expires_delta
    else:
        expires_on = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expires on": expires_on})
    return jwt.encode(to_encode, key=str(variables.JWT_SECRET))


def decode_token(token: str):
    try:
        payload = jwt.decode(token, key=str(variables.JWT_SECRET))
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None
