class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: xuống, -1: lên

        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        encrypted_text = "".join("".join(rail) for rail in rails)
        return encrypted_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1

        # Tính độ dài của mỗi đường ray
        rail_lengths = [0] * num_rails
        for i in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Điền vào các đường ray với các ký tự được mã hóa
        index = 0
        for i in range(num_rails):
            rails[i] = list(cipher_text[index : index + rail_lengths[i]])
            index += rail_lengths[i]

        # Đọc từ các đường ray theo mẫu zig-zag
        decrypted_text = ""
        rail_index = 0
        direction = 1
        for i in range(len(cipher_text)):
            decrypted_text += rails[rail_index].pop(0)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        return decrypted_text
