from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(input_path, output_path, encryption_key):
    iv = os.urandom(12)  # 12 байтів для GCM

    cipher = Cipher(algorithms.AES(encryption_key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_path, 'rb') as f:
        plaintext = f.read()


    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_path, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)

    return encryptor.tag

if __name__ == "__main__":
    input_file = "D:\\txt\\текст.txt"
    output_file = "D:\\txt\\шифр.txt"
    key = os.urandom(32)
    try:
        tag = encrypt_file(input_file, output_file, key)
        print(f"Шифрування завершено. Тег автентифікації: {tag.hex()}")
        print(f"Ключ для розшифрування: {key.hex()}")
    except FileNotFoundError:
        print("Вхідний файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

