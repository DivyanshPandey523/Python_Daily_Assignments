# Mini Project: QR Code Generator
# Install the required library before running:
# pip install "qrcode[pil]"

import qrcode

# Take text or a website link from the user
qr_text = input("Enter text or a website link: ")

# Create the QR code
qr_code = qrcode.make(qr_text)

# Save the QR code as an image
file_name = "my_qr_code.png"
qr_code.save(file_name)

print("QR code created successfully!")
print("Saved as:", file_name)
