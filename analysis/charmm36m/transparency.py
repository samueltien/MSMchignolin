from pymol import cmd

cmd.bg_color("white")
cmd.color("cyan", "resi 1-10")

# Enable all states (so we can see all frames at once)
cmd.set("all_states", "on")

# Get the total number of frames
num_frames = cmd.count_states("All")

# Loop through frames, create separate objects, and set transparency
for i in range(1, num_frames + 1):
    obj_name = f"frame_{i}"
    cmd.create(obj_name, "All", i)  # Extract individual frame as object
    
    if i == 3:  # Make the second frame fully opaque
        cmd.set("cartoon_transparency", 0.0, obj_name)
    else:  # Make all other frames highly transparent
        cmd.set("cartoon_transparency", 0.9, obj_name)

# Hide the original trajectory object to avoid duplicates
#cmd.hide("everything", "All")
