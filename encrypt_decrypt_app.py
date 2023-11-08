import streamlit as st
import random
import string

# Set the page to wide mode
st.set_page_config(layout="wide")

# Title for the web app
st.title("Encrypt-Decrypt Text Application: Caesar Cipher Algorithm")
st.markdown('''
    With this application, you can Encrypt and Decrypt text using the Caesar Cipher algorithm, 
    which is a cryptographic technique that is carried out by substituting each letter of the 
    message to be encrypted by shifting the order as the key. This algorithm is no longer very 
    good to apply because it is easy to guess, but the algorithm is very Easy to Understand, 
    Simple, Fast, and Can be Used as Simple Security for purposes such as storing username 
    and password, sending secret messages, and others.
    '''
    , unsafe_allow_html = True)

# Build tabs
tab1, tab2 = st.tabs(["Caesar Cipher 1", "Caesar Cipher 2"])

# CAESAR CIPHER 1
with tab1:
    # st.subheader("Caesar Cipher 1")
    st.markdown('''
        <p style="color: gray;"> User needs to define the key for shifting characters. 
        A "+" shift means the character shifts to the Right. "-" means the character shifts to 
        the Left. </p>
        '''
        , unsafe_allow_html=True)
    # checkbox = st.checkbox('See Video Example', key = "checkbox_1")
    # if checkbox:
    #     video_file = open('myvideo.mp4', 'rb')
    #     video_bytes = video_file.read()
    #     st.video(video_bytes)

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
    # Requesting text input that you want to ENCRYPT / DECRYPT
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
        st.markdown(f"Encrypted Text: <br> {encrypted_text}", unsafe_allow_html=True)

    # Text Decryption Button
    if st.button("Decrypt Text", key = "Decryption_1"):
        decrypted_text = decrypt_1(text, key)
        st.markdown(f"Decrypted Text: <br> {decrypted_text}", unsafe_allow_html=True)

# CAESAR CIPHER 2
with tab2:
    # st.subheader("Caesar Cipher 2")
    st.markdown('''
        <p style="color: gray;"> User just needs to Enter a message to Encrypt 
        / Decrypt. The Key has been DETERMINED. If you want to see the Key, look at the 
        source code. </p>
        '''
        , unsafe_allow_html=True)

    # checkbox = st.checkbox('See Video Example', key = "checkbox_2")
    # if checkbox:
    #     video_file = open('myvideo.mp4', 'rb')
    #     video_bytes = video_file.read()
    #     st.video(video_bytes)
    
    # Character and Key Definition
    chars = " " + string.ascii_letters + string.digits + string.punctuation
    chars = list(chars)
    # key = chars.copy()

    # # Randomize the key
    # random.shuffle(key)

    # Save Key
    # key = ['0', 'Y', '/', '9', 'a', 'D', 'M', 
    #         'V', 'b', 'K', '#', 'Z', 'R', '{', 'G', 
    #         '%', '2', 'i', '-', 'q', '?', 'Q', '&', 
    #         '`', 'U', 'P', '}', '(', 'n', '5', 'j', 
    #         ',', '4', 'g', ')', 'f', 'B', 'L', 'e', 
    #         'w', 'l', 'c', 'k', '+', ']', 'S', '3', 
    #         'W', '$', 's', 'v', 'T', 'r', 'p', 'J', 
    #         '8', '~', 'O', '1', '\\', 'E', 'F', '=', 
    #         "'", 'X', '^', '!', 'A', '|', 'o', '_', 
    #         'N', '<', 'C', 'u', 't', '6', '>', '7', 
    #         'm', ';', '[', '.', '@', 'd', 'I', '"', 
    #         'H', 'h', ' ', 'z', ':', 'y', 'x', '*']
    key = ['0', 'Y', '/', '9', 'a', 'D', 'M', 
            'V', 'b', 'K', '#', 'Z', 'R', '{', 'G', 
            '%', '2', 'i', '-', 'q', '?', 'Q', '&', 
            '`', 'U', 'P', '}', '(', 'n', '5', 'j', 
            ',', '4', 'g', ')', 'f', 'B', 'L', 'e', 
            'w', 'l', 'c', 'k', '+', ']', 'S', '3', 
            'W', '$', 's', 'v', 'T', 'r', 'p', 'J', 
            '8', '~', 'O', '1', '\\', 'E', 'F', '=', 
            "'", 'X', '^', '!', 'A', '|', 'o', '_', 
            'N', '<', 'C', 'u', 't', '6', '>', '7', 
            'm', ';', '[', '.', '@', 'd', 'I', '"', 
            'H', 'h', ' ', 'z', ':', 'y', 'x', '*']

    # See Chars and Key
    # st.write(f"chars : {chars}")
    # st.write(f"key   : {key}")

    # Encryption_2 Function
    def encrypt_2(plain_text):
        cipher_text = ""
        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]
        st.markdown(f"Encrypted Text: <br> {cipher_text}", unsafe_allow_html=True)

    # Decryption_2 Function
    def decrypt_2(cipher_text):
        plain_text = ""
        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]
        st.markdown(f"Decrypted Text: <br> {plain_text}", unsafe_allow_html=True)

    # Requesting text input that you want to ENCRYPTION / DECRYPTION
    text = st.text_input("Enter a message to Encrypt / Decrypt: ", key = "text_2")

    # Text Encryption Button
    if st.button("Encrypt Text", key = "Encryption_2"):
        encrypt_2(text)

    # Text Decryption Button
    if st.button("Decrypt Text", key = "Decryption_2"):
        decrypt_2(text)

st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
        <a href="https://www.linkedin.com/in/glenhans/" style="text-align: center; font-size: 24px;"> Connect with me😄 </a>
    </div>
    """, unsafe_allow_html=True)
