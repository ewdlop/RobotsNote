import math

def inverse_kinematics(x, y, l1, l2):
    # Calculate the distance from the origin to the point (x, y)
    r = math.sqrt(x**2 + y**2)
    
    # Check if the point is reachable
    if r > (l1 + l2):
        raise ValueError("The point is out of reach")

    # Calculate the angles using the law of cosines
    cos_angle2 = (r**2 - l1**2 - l2**2) / (2 * l1 * l2)
    sin_angle2 = math.sqrt(1 - cos_angle2**2)  # sin^2(theta) + cos^2(theta) = 1

    angle2 = math.atan2(sin_angle2, cos_angle2)

    k1 = l1 + l2 * cos_angle2
    k2 = l2 * sin_angle2

    angle1 = math.atan2(y, x) - math.atan2(k2, k1)

    return angle1, angle2

# Example usage
x, y = 3, 4
l1, l2 = 5, 5

try:
    angle1, angle2 = inverse_kinematics(x, y, l1, l2)
    print(f"Joint angles are: theta1 = {math.degrees(angle1):.2f} degrees, theta2 = {math.degrees(angle2):.2f} degrees")
except ValueError as e:
    print(e)
