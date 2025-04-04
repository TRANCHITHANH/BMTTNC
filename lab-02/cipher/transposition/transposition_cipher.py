class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt_text(self, text, key):
        encrypted_text = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += key
        return ''.join(encrypted_text)

    def decrypt_text(self, text, key):
        num_columns = key
        num_rows = len(text) // key + (1 if len(text) % key else 0)  
        num_shaded_boxes = (num_columns * num_rows) - len(text)  

        decrypted_text = [''] * num_rows 
        col, row = 0, 0

        for symbol in text:
            decrypted_text[row] += symbol
            row += 1 
            if row == num_rows or (row == num_rows - 1 and col >= num_columns - num_shaded_boxes):
                row = 0  
                col += 1  

        return ''.join(decrypted_text)
