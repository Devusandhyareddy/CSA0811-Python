import cv2
from matplotlib import pyplot as plt

# File Path (Update with your actual path)
file_path = r'C:\Deer.png'

# Load the Image
im = cv2.imread(file_path)

# Check if the image is loaded successfully
if im is None:
    print("Error: Could not read the image. Please check the file path.")
else:
    # Continue with image processing
    edges = cv2.Canny(im, 100, 300)

    # Create a 2x2 subplot grid
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Plot the original image
    axs[0, 0].imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Original Image')

    # Plot Canny edges with different colormaps
    axs[0, 1].imshow(edges, cmap='gray')
    axs[0, 1].set_title('Grayscale')

    axs[1, 0].imshow(edges, cmap='viridis')
    axs[1, 0].set_title('Viridis')

    axs[1, 1].imshow(edges, cmap='plasma')
    axs[1, 1].set_title('Plasma')

    # Remove ticks for all subplots
    for ax in axs.flat:
        ax.set_xticks([])
        ax.set_yticks([])

    # Adjust layout for better spacing
    plt.tight_layout()

    # Show the plot
    plt.show()
