class VigenereCipher:
    """
    Encodes and decodes text using the Vigenere cipher.
    """

    def __init__(self):
        """
        Initializes the VigenereCipher.
        """
        pass

    def vigenere_encrypt(self, plain_text: str, key: str) -> str:
        """
        Encrypts the given text using the Vigenere cipher with the specified key.

        Args:
            plain_text: The text to encrypt.
            key: The key for encryption.

        Returns:
            The encrypted text.
        """
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord("A")
                if char.isupper():
                    encrypted_text += chr(
                        (ord(char) - ord("A") + key_shift) % 26 + ord("A")
                    )
                else:
                    encrypted_text += chr(
                        (ord(char) - ord("a") + key_shift) % 26 + ord("a")
                    )
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text: str, key: str) -> str:
        """
        Decrypts the given text using the Vigenere cipher with the specified key.

        Args:
            encrypted_text: The text to decrypt.
            key: The key for decryption.

        Returns:
            The decrypted text.
        """
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord("A")
                if char.isupper():
                    decrypted_text += chr(
                        (ord(char) - ord("A") - key_shift + 26) % 26 + ord("A")
                    )
                else:
                    decrypted_text += chr(
                        (ord(char) - ord("a") - key_shift + 26) % 26 + ord("a")
                    )
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
