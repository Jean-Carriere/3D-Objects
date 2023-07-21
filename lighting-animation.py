import bpy
from math import radians, cos, sin

# Create new point lighting
bpy.ops.object.light_add(type='POINT', location=(0, 0, 10))

# Get the created light
light = bpy.context.object

# Set the light's energy
light.data.energy = 1  # Adjust this value as needed

# Point the light downwards and shift it behind the camera
light.rotation_euler = (radians(90), 0, radians(180))
light.location = (0, -15, 25)

# Set the total frames for the animation
total_frames = 240
bpy.context.scene.frame_end = total_frames

# Create a camera at a fixed distance from the block
camera_location = (40, 0, 30)  # Adjust this value as needed
bpy.ops.object.camera_add(location=camera_location)
camera = bpy.context.object

# Rotate the camera's yaw by 90 degrees and pitch down by 20 degrees
camera.rotation_euler = (radians(70), 0, radians(90))

# Animate the camera to orbit around the block
for i in range(total_frames + 1):
    # Set the scene to the right frame
    bpy.context.scene.frame_set(i)

    # Calculate the new location and rotation for the camera
    angle = radians(i / 2)
    new_location = (40 * cos(angle), 40 * sin(angle), 15)  # Adjust this value as needed
    new_rotation = (radians(77), 0, angle + radians(90))

    # Set the new location and rotation for the camera
    camera.location = new_location
    camera.rotation_euler = new_rotation

    # Insert keyframes for the location and rotation properties
    camera.keyframe_insert(data_path="location")
    camera.keyframe_insert(data_path="rotation_euler")
