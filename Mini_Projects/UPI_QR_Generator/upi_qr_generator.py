# Mini Project: UPI QR Code Generator
# Install the required library before running:
# pip install "qrcode[pil]"
#
# This program creates a UPI payment QR code.
# Check the UPI ID, receiver name and amount carefully before using it.

import qrcode
from urllib.parse import quote

upi_id = input("Enter your UPI ID: ")
payee_name = input("Enter receiver name: ")
amount = input("Enter amount (leave blank if not needed): ")

# Prepare the UPI payment link
payment_link = (
    "upi://pay?pa=" + quote(upi_id)
    + "&pn=" + quote(payee_name)
    + "&cu=INR"
)

if amount != "":
    payment_link = payment_link + "&am=" + quote(amount)

# Create and save the QR code
qr_code = qrcode.make(payment_link)
file_name = "upi_payment_qr.png"
qr_code.save(file_name)

print("UPI QR code created successfully!")
print("Saved as:", file_name)
