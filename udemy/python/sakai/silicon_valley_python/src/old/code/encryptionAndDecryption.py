import string
import random

from Crypto.Cipher import AES


key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size))

iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size))


# plaintext = "ojfosjdflseljf;osjdl;vsdoij"
# # ivは初期ベクトル
# # ブロックごとに暗号化するの16文字の塊で暗号化する　
# cipher = AES.new(key, AES.MODE_CBC, iv)
# # 足りない文字数を整える
# padding_length = AES.block_size - len(plaintext) % AES.block_size　
# plaintext += chr(padding_length) * padding_length
#
# # 文字列を暗号化する　出力
# cipher_text = cipher.encrypt(plaintext)
# print(cipher_text)
#
#
# # 複合する
# cipher2 = AES.new(key, AES.MODE_CBC, iv)
# decrypted_text = cipher2.decrypt(cipher_text)
# print(decrypted_text)
# print(decrypted_text[-1])
# print(decrypted_text[:-decrypted_text[-1]])








with open('/Users/miyazonoeiji/projects/python/udemy/siliconValleyStyle/code/plaintext', 'r') as f, open('/Users/miyazonoeiji/projects/python/udemy/siliconValleyStyle/code/enc.dat', 'wb') as e:
    plaintext = f.read()
    # ivは初期ベクトル
    # ブロックごとに暗号化するの16文字の塊で暗号化する　
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 足りない文字数を整える
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length

    # 文字列を暗号化する　出力
    cipher_text = cipher.encrypt(plaintext)
    e.write(cipher_text)


# 複合する
with open('/Users/miyazonoeiji/projects/python/udemy/siliconValleyStyle/code/enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))
