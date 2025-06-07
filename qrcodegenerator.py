import qrcode
import pygame
import sys

# Get user input
data = input("Enter text or URL for QR code: ")

# Generate QR code with custom colors
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an image with black foreground and white background
qr_img = qr.make_image(fill='black', back_color='white')

# Save the QR code as a file
qr_img.save("qr_code.png")

# Initialize pygame
pygame.init()

# Load the QR code into Pygame
qr_surface = pygame.image.load("qr_code.png")
width, height = qr_surface.get_size()

# Create Pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("QR Code Viewer")

# Game loop to display QR code
running = True
while running:
    screen.fill((255, 255, 255))  # Ensure white background
    screen.blit(qr_surface, (0, 0))  # Display the QR code

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()