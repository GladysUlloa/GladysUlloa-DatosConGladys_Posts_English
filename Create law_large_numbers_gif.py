import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import imageio
import os

# Aesthetic configuration
sns.set(style="whitegrid")
plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 16

# Create temporary folder for images
if not os.path.exists("frames"):
    os.makedirs("frames")

# Parameters
mu = 50       # population mean
sigma = 10    # standard deviation
sample_size = 1000  # total simulated data points
samples = np.random.normal(mu, sigma, sample_size)

# Initialize list to save images
filenames = []

# Create images for each incremental sample size (smooth animation)
for n in range(10, sample_size+1, 5):  # smaller step for continuous animation
    sample_mean = np.mean(samples[:n])

    plt.figure(figsize=(8, 5))

    # Histogram with edges and soft aesthetics
    sns.histplot(samples[:n],
                 bins=30,
                 kde=True,
                 color="#4C72B0",
                 edgecolor="black",  # bar borders
                 linewidth=0.5,
                 alpha=0.7)

    # Population mean line
    plt.axvline(mu, color='green', linestyle='--', linewidth=2, label=f'Population mean: {mu}')

    # Current sample mean line
    plt.axvline(sample_mean, color='red', linestyle='-', linewidth=2, label=f'Sample mean (n={n}): {sample_mean:.2f}')

    # Chart aesthetics
    plt.title("Law of Large Numbers", fontsize=18)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend(loc="upper right", fontsize=10)
    plt.tight_layout()

    # Save frame
    filename = f"frames/frame_{n}.png"
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()

# Create continuous GIF
with imageio.get_writer("law_large_numbers.gif", mode='I', duration=0.04) as writer:  # smoother speed
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Remove intermediate frames
for filename in filenames:
    os.remove(filename)

print("✅ GIF generated with continuous animation: law_large_numbers.gif")
