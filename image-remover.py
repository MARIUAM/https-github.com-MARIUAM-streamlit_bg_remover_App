# import streamlit as st
# from rembg import remove
# from PIL import Image
# from io import BytesIO
# import base64

# st.set_page_config(layout="wide", page_title="Image Background Remover")

# st.write("## Remove background from your image")
# st.write(
#     ":dog: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar. This code is open source and available [here](https://github.com/tyler-simons/BackgroundRemoval) on GitHub. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
# )
# st.sidebar.write("## Upload and download :gear:")

# MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# # Download the fixed image
# def convert_image(img):
#     buf = BytesIO()
#     img.save(buf, format="PNG")
#     byte_im = buf.getvalue()
#     return byte_im


# def fix_image(upload):
#     image = Image.open(upload)
#     col1.write("Original Image :camera:")
#     col1.image(image)

#     fixed = remove(image)
#     col2.write("Fixed Image :wrench:")
#     col2.image(fixed)
#     st.sidebar.markdown("\n")
#     st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


# col1, col2 = st.columns(2)
# my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# if my_upload is not None:
#     if my_upload.size > MAX_FILE_SIZE:
#         st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
#     else:
#         fix_image(upload=my_upload)
# else:
#     fix_image("./zebra.jpg")
# import streamlit as st
# from rembg import remove
# from PIL import Image
# from io import BytesIO
# import base64
# import os

# def convert_image(img):
#     buf = BytesIO()
#     img.save(buf, format="PNG")
#     byte_im = buf.getvalue()
#     return byte_im

# def fix_image(upload):
#     image = Image.open(upload)
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Original Image")
#         st.image(image, use_column_width=True)
    
#     fixed = remove(image)
    
#     with col2:
#         st.subheader("Background Removed")
#         st.image(fixed, use_column_width=True)
    
#     st.sidebar.download_button("Download Image", convert_image(fixed), "fixed.png", "image/png")

# # App Configuration
# st.set_page_config(page_title="Image Background Remover", layout="wide")

# st.title("🖼️ AI-Powered Background Remover")
# st.markdown(
#     "Remove the background from any image effortlessly. Upload your image and get a transparent PNG in seconds! 🎨"
# )

# st.sidebar.header("Upload Image")
# st.sidebar.write("Drag & drop or select an image file.")

# # File Uploader
# my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

# if my_upload is not None:
#     fix_image(my_upload)
# else:
#     st.info("Please upload an image to remove the background.")


# import streamlit as st
# from rembg import remove
# from PIL import Image
# from io import BytesIO
# import base64
# import os

# def convert_image(img):
#     buf = BytesIO()
#     img.save(buf, format="PNG")
#     byte_im = buf.getvalue()
#     return byte_im

# def fix_image(upload):
#     image = Image.open(upload)
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Original Image")
#         st.image(image, use_column_width=True)
    
#     fixed = remove(image)
    
#     with col2:
#         st.subheader("Background Removed")
#         st.image(fixed, use_column_width=True)
    
#     st.sidebar.download_button("Download Image", convert_image(fixed), "fixed.png", "image/png")

# # App Configuration
# st.set_page_config(page_title="Image Background Remover", layout="wide")

# st.title("🖼️ AI-Powered Background Remover")
# st.markdown(
#     "Remove the background from any image effortlessly. Upload your image and get a transparent PNG in seconds! 🎨"
# )

# # User Authentication
# st.sidebar.header("User Authentication")
# login_status = st.sidebar.radio("Login / Signup", ["Login", "Signup"])
# if login_status == "Signup":
#     username = st.sidebar.text_input("Enter a username")
#     password = st.sidebar.text_input("Enter a password", type="password")
#     if st.sidebar.button("Sign Up"):
#         st.sidebar.success("Account created successfully! Please log in.")
# elif login_status == "Login":
#     username = st.sidebar.text_input("Username")
#     password = st.sidebar.text_input("Password", type="password")
#     if st.sidebar.button("Login"):
#         st.sidebar.success(f"Welcome, {username}!")

# st.sidebar.header("Upload Image")
# st.sidebar.write("Drag & drop or select an image file.")

# # Additional Features
# st.sidebar.subheader("Features:")
# st.sidebar.markdown("✔️ Drag & Drop Upload")
# st.sidebar.markdown("✔️ Dark Mode Support")
# st.sidebar.markdown("✔️ High-Quality Processing")
# st.sidebar.markdown("✔️ Instant Preview")
# st.sidebar.markdown("✔️ User Authentication")
# st.sidebar.markdown("✔️ Multi-Format Support")
# st.sidebar.markdown("✔️ Secure Image Handling")
# st.sidebar.markdown("✔️ Fast & Efficient")
# st.sidebar.markdown("✔️ AI-Powered Removal")
# st.sidebar.markdown("✔️ Download Processed Image")

# # File Uploader
# my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

# if my_upload is not None:
#     fix_image(my_upload)
# else:
#     st.info("Please upload an image to remove the background.")


import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64
import os

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload, bg_choice=None):
    image = Image.open(upload)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(image, use_column_width=True)
    
    fixed = remove(image)
    
    if bg_choice:
        bg_image = Image.open(bg_choice).resize(fixed.size)
        fixed = Image.alpha_composite(bg_image.convert("RGBA"), fixed.convert("RGBA"))
    
    with col2:
        st.subheader("Processed Image")
        st.image(fixed, use_column_width=True)
    
    st.sidebar.download_button("Download Image", convert_image(fixed), "processed.png", "image/png")

# App Configuration
st.set_page_config(page_title="Image Background Remover", layout="wide")

st.title("🖼️ AI-Powered Background Remover")
st.markdown("Remove the background from any image effortlessly and replace it with a custom background! 🎨")

# User Authentication
st.sidebar.header("User Authentication")
login_status = st.sidebar.radio("Login / Signup", ["Login", "Signup"])
if login_status == "Signup":
    username = st.sidebar.text_input("Enter a username")
    password = st.sidebar.text_input("Enter a password", type="password")
    if st.sidebar.button("Sign Up"):
        st.sidebar.success("Account created successfully! Please log in.")
elif login_status == "Login":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        st.sidebar.success(f"Welcome, {username}!")

st.sidebar.header("Upload Image")
st.sidebar.write("Drag & drop or select an image file.")

# Background Selection
st.sidebar.header("Select Background")
bg_options = {
    "None (Transparent)": None,
    "Sky": "sky.png",
    "Beach": "Beach.png",
    "City": "city.png",
    "Nature": "Abstract Background.png"
}
selected_bg = st.sidebar.selectbox("Choose a background", list(bg_options.keys()))

# File Uploader
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

if my_upload is not None:
    fix_image(my_upload, bg_options[selected_bg])
else:
    st.info("Please upload an image to remove the background.")
