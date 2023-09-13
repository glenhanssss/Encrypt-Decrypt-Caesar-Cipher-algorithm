import streamlit as st
import random
import string

# Set the page to wide mode
st.set_page_config(layout="wide")

# Title for the web app
# st.title("Single/ Multiple Linear Regression Application")
# st.markdown("<strong>The application reads the first <em>ROW</em> in your file as the <em>Column Title (Variable Name)</em> for each <em>COLUMN</em> in the dataset. So make sure that the first <em>ROW</em> in your file is the name of each <em>Column Title (Variable Name)</em> in the dataset. Also, make sure that every cell in your file is Valid (all cells are filled and there are no duplicates) for better analysis.</strong>", unsafe_allow_html=True)
# st.markdown("<strong>This application allows you to carry out linear regression analysis, both single linear regression and multiple linear regression. The analysis results obtained, namely the regression model and all the visualizations displayed, can help you predict unknown data values using other related and known data values. This really helps businesses, industry, trade, and other sectors.</strong>", unsafe_allow_html=True)

########################################################

# CAESAR CIPHER 1

# Encryption_1 Function
def encrypt_1(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalnum() or not char.isascii():
            is_upper = char.isupper()
            char = char.lower()
            if char.isnumeric():
                encrypted_char = chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

# Decryption_1 Function
def decrypt_1(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalnum() or not char.isascii():
            is_upper = char.isupper()
            char = char.lower()
            if char.isnumeric():
                decrypted_char = chr(((ord(char) - ord('0') - shift) % 10) + ord('0'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

# Requesting text input that you want to ENCRYPTION / DECRYPTION
text = st.text_input("Enter a message to Encrypt / Decrypt: ", key = "text_1")

# Requesting Key value and Create Key Shift Condition (shift of Encryption_1 and Decryption_1 Functions)
key = None
while not isinstance(key, int):
    try:
        key = st.number_input("Many keys are Shifted: ", value=0, step=1)
    except ValueError:
        st.error()

# Text Encryption Button
if st.button("Encrypt Text", key = "Encryption_1"):
    encrypted_text = encrypt_1(text, key)
    st.write("Teks terenkripsi:", encrypted_text)

# Text Decryption Button
if st.button("Decrypt Text", key = "Decryption_1"):
    decrypted_text = decrypt_1(text, key)
    st.write("Teks terdekripsi:", decrypted_text)

########################################################

# CAESAR CIPHER 2

# Character and Key Definition
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
# key = chars.copy()

# # Randomize the key
# random.shuffle(key)

# Save Key
key = ['e', '$', 'g', 'h', 'd', 'A', 'r', '3', 'y', 'J', 'v', 'I', 'O', '1', '5', ',', 'S', '<', 'L', '(', ':', 'n', 'Z', '\\', '[', 'M', '?', '.', 'x', 'P', '{', '_', '-', 'l', '>', 'N', 'c', '}', '9', '%', 'b', 't', '&', 'R', '/', '#', '!', 'k', 'w', ';', '7', '8', 'H', '~', 'W', '`', '|', 'a', 's', '"', 'j', '6', 'E', 'K', 'G', 'D', 'B', 'f', 'V', '*', '@', 'u', 'X', 'p', 'm', 'Q', '+', 'o', '2', 'T', ' ', 'z', '0', ']', '4', 'C', '^', '=', 'F', 'Y', 'i', 'q', "'", 'U', ')']

# See Key
# st.write(f"chars : {chars}")
# st.write(f"key   : {key}")

# Encryption_2 Function
def encrypt_2(plain_text):
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    st.write(f"Teks terenkripsi: {cipher_text}")

# Decryption_2 Function
def decrypt_2(cipher_text):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    st.write(f"Teks terenkripsi: {plain_text}")

# Requesting text input that you want to ENCRYPTION / DECRYPTION
text = st.text_input("Enter a message to Encrypt / Decrypt: ", key = "text_2")

# Text Encryption Button
if st.button("Encrypt Text", key = "Encryption_2"):
    encrypt_2(text)

# Text Decryption Button
if st.button("Decrypt Text", key = "Decryption_2"):
    decrypt_2(text)

tab1, tab2 = st.tabs(["CAESAR CIPHER 1", "CAESAR CIPHER 2"])

# with tab1:
#    st.header("CAESAR CIPHER 1")

# with tab2:
#    st.header("CAESAR CIPHER 2")