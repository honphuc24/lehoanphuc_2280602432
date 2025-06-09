class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        seen = set()
        matrix = []
        # Chỉ thêm ký tự mới vào ma trận
        for ch in key:
            if ch not in seen and ch.isalpha():
                seen.add(ch)
                matrix.append(ch)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for ch in alphabet:
            if ch not in seen:
                matrix.append(ch)
                if len(matrix) == 25:
                    break

        # Chia thành 5×5
        return [matrix[i:i+5] for i in range(0,25,5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""
        i = 0
        while i < len(plain_text):
            if i + 1 < len(plain_text):
                a = plain_text[i]
                b = plain_text[i+1]
                row1, col1 = self.find_letter_coords(matrix, a)
                row2, col2 = self.find_letter_coords(matrix, b)
                if row1 == row2:  # cùng hàng
                    encrypted_text += matrix[row1][(col1+1) % 5]
                    encrypted_text += matrix[row2][(col2+1) % 5]
                elif col1 == col2:  # cùng cột
                    encrypted_text += matrix[(row1+1) % 5][col1]
                    encrypted_text += matrix[(row2+1) % 5][col2]
                else:  # tạo thành hình chữ nhật
                    encrypted_text += matrix[row1][col2]
                    encrypted_text += matrix[row2][col1]
                i += 2
            else:
                encrypted_text += plain_text[i]
                i += 1
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        decrypted_text = ""
        i = 0
        while i < len(cipher_text):
            if i + 1 < len(cipher_text):
                a = cipher_text[i]
                b = cipher_text[i + 1]
                row1, col1 = self.find_letter_coords(matrix, a)
                row2, col2 = self.find_letter_coords(matrix, b)
                if row1 == row2:
                    decrypted_text += matrix[row1][(col1 - 1 + 5) % 5]
                    decrypted_text += matrix[row2][(col2 - 1 + 5) % 5]
                elif col1 == col2:
                    decrypted_text += matrix[(row1 - 1 + 5) % 5][col1]
                    decrypted_text += matrix[(row2 - 1 + 5) % 5][col2]
                else:
                    decrypted_text += matrix[row1][col2]
                    decrypted_text += matrix[row2][col1]
                i += 2
            else:
                decrypted_text += cipher_text[i]
                i += 1
        return decrypted_text
