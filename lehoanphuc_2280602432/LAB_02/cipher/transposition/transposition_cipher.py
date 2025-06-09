class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        """
        Encrypts a plain_text using the Transposition Cipher.
        It pads with '_' to form a complete rectangle.
        """
        plain_text = text.replace(" ", "").upper()
        num_columns = key
        num_rows = (len(plain_text) + num_columns - 1) // num_columns

        matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

        k = 0
        for r in range(num_rows):
            for c in range(num_columns):
                if k < len(plain_text):
                    matrix[r][c] = plain_text[k]
                    k += 1
                else:
                    matrix[r][c] = '_' # Padding with '_'

        cipher_text = ""
        for c in range(num_columns):
            for r in range(num_rows):
                cipher_text += matrix[r][c]
        return cipher_text

    def decrypt(self, text, key):
        """
        Decrypts a cipher_text using the Transposition Cipher.
        This reverses the encryption process, handling the padding.
        """
        num_cols = key
        # For decryption, num_rows should be calculated based on the cipher_text length
        # which includes padding, so it should form a complete rectangle.
        num_rows = (len(text) + num_cols - 1) // num_cols

        # Create an empty matrix to reconstruct the plaintext
        matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

        # Fill the matrix column by column using the characters from the ciphertext
        # This is because the ciphertext was formed by reading columns.
        k = 0
        for col_idx in range(num_cols):
            for row_idx in range(num_rows):
                # Ensure we don't go out of bounds if there's any discrepancy
                if k < len(text):
                    matrix[row_idx][col_idx] = text[k]
                    k += 1

        decrypted_text = ""
        # Read the matrix row by row to retrieve the original plaintext
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                char = matrix[row_idx][col_idx]
                # Remove padding characters ('_') if they exist
                if char != '_':
                    decrypted_text += char
        return decrypted_text