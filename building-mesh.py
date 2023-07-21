import bpy
import bmesh

# Define the building dimensions
num_rows = 2  # Number of rows in the grid
num_cols = 1  # Number of columns in the grid
building_width = 9
building_length = 2.5
num_floors = 3
floor_height = 3.88

# Create a new mesh and link it to the scene
mesh = bpy.data.meshes.new(name="BuildingMesh")
obj = bpy.data.objects.new("Building", mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
mesh = bpy.context.object.data
bm = bmesh.new()

# Add building spaces to the grid
for row in range(num_rows):
    for col in range(num_cols):
        # Calculate position of the building
        x_pos = col * building_width
        y_pos = row * building_length
        for floor in range(num_floors):
            z_pos = floor * floor_height
            # Create vertices of the floor
            v1 = bm.verts.new((x_pos, y_pos, z_pos))
            v2 = bm.verts.new((x_pos, y_pos + building_length, z_pos))
            v3 = bm.verts.new((x_pos + building_width, y_pos + building_length, z_pos))
            v4 = bm.verts.new((x_pos + building_width, y_pos, z_pos))
            v5 = bm.verts.new((x_pos, y_pos, z_pos + floor_height))
            v6 = bm.verts.new((x_pos, y_pos + building_length, z_pos + floor_height))
            v7 = bm.verts.new((x_pos + building_width, y_pos + building_length, z_pos + floor_height))
            v8 = bm.verts.new((x_pos + building_width, y_pos, z_pos + floor_height))
            # Create faces using the vertices
            bm.faces.new((v1, v2, v3, v4))
            bm.faces.new((v5, v6, v7, v8))
            bm.faces.new((v1, v2, v6, v5))
            bm.faces.new((v2, v3, v7, v6))
            bm.faces.new((v3, v4, v8, v7))
            bm.faces.new((v4, v1, v5, v8))

# Update the mesh with the new vertices and faces
bm.to_mesh(mesh)
bm.free()

# Move the object to the origin
obj.location = (-4.5, -2.5, 0)

# Recalculate the object's origin to the center of the mesh
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
