import numpy as np

def translation_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def rotation_matrix(theta):
    return np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ])

def transform_point(point, transform):
    # Convert point to homogeneous coordinates
    point_h = np.array([point[0], point[1], 1])
    # Apply transformation
    transformed_point = np.dot(transform, point_h)
    return transformed_point[:2]

# Example usage
point = [1, 2]
tx, ty = 3, 4
theta = math.radians(45)

translation = translation_matrix(tx, ty)
rotation = rotation_matrix(theta)

# Apply translation and then rotation
transform = np.dot(rotation, translation)
new_point = transform_point(point, transform)

print(f"Original point: {point}")
print(f"Transformed point: {new_point}")
