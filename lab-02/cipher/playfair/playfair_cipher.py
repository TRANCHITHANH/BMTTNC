class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key) + remaining_letters
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_char_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, key):
        matrix = self.create_playfair_matrix(key)
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            if len(pair) == 1:
                pair += "X"

            if not any(pair[0] in row for row in matrix) or not any(pair[1] in row for row in matrix):
                continue

            row1, col1 = self.find_char_coords(matrix, pair[0])
            row2, col2 = self.find_char_coords(matrix, pair[1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, key):
        matrix = self.create_playfair_matrix(key)
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_char_coords(matrix, pair[0])
            row2, col2 = self.find_char_coords(matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        banro = ""
        for i in range(0, len(decrypted_text) - 2, 2):
            if decrypted_text[i] == decrypted_text[i + 1]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + decrypted_text[i + 1]
        
        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2] + decrypted_text[-1]
        
        return banro
