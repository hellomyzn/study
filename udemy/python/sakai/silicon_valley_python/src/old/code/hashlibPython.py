import base64
import os
import hashlib


# passwordをハッシュ化する bytes()で変換する必要がある
# print(hashlib.sha256(b'password').hexdigest())
#
# print(hashlib.sha256(b'test').hexdigest())
# print(hashlib.sha256(b'test2').hexdigest())

user_name = 'user1'
user_pass = 'password'
db = {}


# ハッシュ化して、悪意のあるユーザーが複合しようとしてもできない
def get_digest(password):
    password = bytes(password, 'utf-8')
    digest = hashlib.sha256(password).hexdigest()
    return digest


db[user_name] = get_digest(user_pass)


def is_login(user_name, password):
    return get_digest(password) == db[user_name]


# 上がTrueになり下がFalseになる
print(is_login(user_name, user_pass))
print(is_login(user_name, 'test'))


# ソルトを作成
salt = base64.b64encode(os.urandom(32))

# def get_digest(password):
#     password = bytes(password, 'utf-8')
#     digest = hashlib.sha256(salt + password).hexdigest()

      # digestを何回もhash化して何回目のhashなのかをわからなくする
#     for _ in range(10000):
#         digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
#         print(digest)
#     print(digest)
#     return digest


# get_digestと同じ処理の関数
digest = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 10000)

db[user_name] = digest

# db[user_name] = get_digest(user_pass)

def is_login(user_name, password):
    digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(password, 'utf-8'), salt, 10000)
    # return get_digest(password) == db[user_name]
    return digest == db[user_name]

print(is_login(user_name, user_pass))
