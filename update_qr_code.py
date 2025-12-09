import qrcode
import sys

def generate_qr_code(url, output_path='potluck-qr-code.png'):
    """
    Generate a QR code for the given URL
    
    Args:
        url: The Google Form URL to encode
        output_path: Path where the QR code image will be saved
    """
    # Create QR code with high error correction
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create the QR code image with custom colors matching the flyer
    img = qr.make_image(fill_color="#2C1810", back_color="white")
    
    # Save the QR code
    img.save(output_path)
    print(f"✓ QR code generated successfully!")
    print(f"✓ Saved to: {output_path}")
    print(f"✓ URL encoded: {url}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If URL is provided as command line argument
        form_url = sys.argv[1]
    else:
        # Interactive mode
        print("=" * 60)
        print("QR Code Generator for Music & Soul Vibes Flyer")
        print("=" * 60)
        print("\nPaste your Google Form URL below:")
        form_url = input("URL: ").strip()
    
    if not form_url:
        print("Error: No URL provided!")
        sys.exit(1)
    
    # Generate the QR code
    generate_qr_code(form_url, '/mnt/user-data/outputs/potluck-qr-code.png')
    print("\n✓ Your flyer is ready with the updated QR code!")
