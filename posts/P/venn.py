import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, PathPatch
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
import os
import tempfile
from PIL import Image
import glob
from moviepy.editor import ImageSequenceClip
import matplotlib.cm as cm
from matplotlib.colors import to_rgba

# Set backend to Agg which is more compatible with saving to files
plt.switch_backend('Agg')

# Create output directory for frames
os.makedirs("venn_frames", exist_ok=True)

# Function to create a single frame
def create_frame(frame_num, total_frames=360):
    # Calculate the time value (t) based on frame number
    t = frame_num / (total_frames / 15)  # 15 seconds total duration
    
    # Create figure with fixed size and DPI
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
    fig.set_facecolor('white')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Define the circles
    r = 1.8
    circle_A = Circle((-1.5, 0.5), r, alpha=0.4, edgecolor='black', facecolor='red', linewidth=1.5)
    circle_B = Circle((0, -0.3), r, alpha=0.4, edgecolor='black', facecolor='blue', linewidth=1.5)
    circle_C = Circle((1.5, 0.5), r, alpha=0.4, edgecolor='black', facecolor='green', linewidth=1.5)
    
    # Define the universe (entire population)
    universe = Rectangle((-4, -3.5), 8, 7, fill=True, edgecolor='black', facecolor='#f0f0f0', 
                         linestyle='--', linewidth=1.5, zorder=-1)
    ax.add_patch(universe)
    
    # Add the circles to the plot
    ax.add_patch(circle_A)
    ax.add_patch(circle_B)
    ax.add_patch(circle_C)
    
    # Add labels with white outline
    label_A = ax.text(-1.5, 1.7, "Coverage A\n(1/4)", fontsize=14, ha='center', fontweight='bold')
    label_A.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    
    label_B = ax.text(0, -2.2, "Coverage B\n(1/3)", fontsize=14, ha='center', fontweight='bold')
    label_B.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    
    label_C = ax.text(1.5, 1.7, "Coverage C\n(5/12)", fontsize=14, ha='center', fontweight='bold')
    label_C.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    
    # Add intersections - these are the pairs of coverages
    if t > 2:
        # Highlight A∩B intersection
        highlight_AB = ax.text(-0.8, 0, "A∩B", fontsize=14, ha='center', color='black')
        highlight_AB.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    
    if t > 3:
        # Highlight B∩C intersection
        highlight_BC = ax.text(0.8, 0, "B∩C", fontsize=14, ha='center', color='black')
        highlight_BC.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    
    if t > 4:
        # Highlight A∩C intersection
        highlight_AC = ax.text(0, 1.0, "A∩C", fontsize=14, ha='center', color='black')
        highlight_AC.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    
    # Add title (always visible)
    title = ax.text(0, 3.5, "Health Plan Coverage Problem", 
                   fontsize=24, ha='center', fontweight='bold')
    
    # Add the problem statement
    if t > 0:
        problem_text = "An employee must choose exactly 2 coverages or none"
        ax.text(0, -3, problem_text, fontsize=14, ha='center')
    
    # Show the equations more visually
    if t > 5:
        # Start highlighting the N region (no coverage)
        # First darken everything outside the circles
        no_coverage_area = Rectangle((-4, -3.5), 8, 7, alpha=0.2, facecolor='gray', zorder=-0.5)
        ax.add_patch(no_coverage_area)
        
        # Then re-add the circles to "cut out" the areas
        ax.add_patch(Circle((-1.5, 0.5), r, alpha=0.4, edgecolor='black', facecolor='red', linewidth=1.5))
        ax.add_patch(Circle((0, -0.3), r, alpha=0.4, edgecolor='black', facecolor='blue', linewidth=1.5))
        ax.add_patch(Circle((1.5, 0.5), r, alpha=0.4, edgecolor='black', facecolor='green', linewidth=1.5))
        
        # Add label for no coverage region
        no_coverage_text = ax.text(3.5, -3, "No Coverage\nRegion (N)", fontsize=14, ha='center', weight='bold')
        no_coverage_text.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
    
    # Show the proportions and what they mean
    if t > 7:
        # Add equations for probabilities
        ax.text(-4, 2.8, "P(A) = 1/4", fontsize=13)
        ax.text(-4, 2.4, "P(B) = 1/3", fontsize=13)
        ax.text(-4, 2.0, "P(C) = 5/12", fontsize=13)
    
    # Show the relationship between the regions
    if t > 9:
        # Draw an equation to show that P(A) = P(A∩B) + P(A∩C)
        ax.text(-4, 1.5, "P(A) = P(A∩B) + P(A∩C)", fontsize=13)
        
        # Add arrows pointing to the intersections
        arrow_AB = ax.annotate("", xy=(-0.8, 0), xytext=(-2.5, 1.5),
                         arrowprops=dict(arrowstyle="->", lw=1.5))
        
        arrow_AC = ax.annotate("", xy=(0, 1.0), xytext=(-2.5, 1.5),
                         arrowprops=dict(arrowstyle="->", lw=1.5))
    
    if t > 10:
        # Show the sum of all regions equals 1
        sum_eq = ax.text(-4, -1.5, "P(A∩B) + P(A∩C) + P(B∩C) + P(N) = 1", fontsize=14, weight='bold')
        
        # Visual representation of solution
        if t > 11:
            # Show that the "no coverage" region is 1/2
            ax.text(-4, -2.0, "P(A) + P(B) + P(C) = 2[P(A∩B) + P(A∩C) + P(B∩C)]", fontsize=13)
    
    # Final solution
    if t > 12:
        # Highlight the solution more prominently
        sol = ax.text(0, -3.5, "P(N) = 1/2", fontsize=24, ha='center', color='red', fontweight='bold')
        sol.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])
        
        # Make the no coverage region more visible
        no_coverage_area = Rectangle((-4, -3.5), 8, 7, alpha=0.3, facecolor='red', zorder=-0.5)
        ax.add_patch(no_coverage_area)
        
        # Re-add the circles to "cut out" the areas
        ax.add_patch(Circle((-1.5, 0.5), r, alpha=0.4, edgecolor='black', facecolor='red', linewidth=1.5))
        ax.add_patch(Circle((0, -0.3), r, alpha=0.4, edgecolor='black', facecolor='blue', linewidth=1.5))
        ax.add_patch(Circle((1.5, 0.5), r, alpha=0.4, edgecolor='black', facecolor='green', linewidth=1.5))
    
    # Save the figure to a file
    frame_path = f"venn_frames/frame_{frame_num:04d}.png"
    plt.tight_layout()
    plt.savefig(frame_path, dpi=100, bbox_inches='tight')
    plt.close(fig)
    
    return frame_path

def main():
    # Set parameters
    fps = 24
    duration = 15  # seconds
    total_frames = fps * duration
    
    print("Generating frames...")
    # Generate all frames
    for i in range(total_frames):
        if i % 24 == 0:  # Print progress every second
            print(f"Creating frame {i}/{total_frames} (second {i//24})")
        create_frame(i, total_frames)
    
    print("Combining frames into video...")
    # Get all frame files in order
    frame_files = sorted(glob.glob("venn_frames/frame_*.png"))
    
    # Create video from frames
    clip = ImageSequenceClip(frame_files, fps=fps)
    clip.write_videofile("health_plan_venn.mp4", fps=fps, codec='libx264')
    
    print("Video created successfully!")

if __name__ == "__main__":
    main()