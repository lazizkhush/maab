import math

class Vector:
    def __init__(self, *components):
        """Initialize a vector with any number of dimensions."""
        self.components = tuple(components)

    def __repr__(self):
        """String representation of the vector."""
        return f"Vector{self.components}"

    def __add__(self, other):
        """Vector addition (element-wise)."""
        if not isinstance(other, Vector):
            raise TypeError("Addition is only supported between two vectors.")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        
        new_components = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __sub__(self, other):
        """Vector subtraction (element-wise)."""
        if not isinstance(other, Vector):
            raise TypeError("Subtraction is only supported between two vectors.")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        
        new_components = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __mul__(self, other):
        """Dot product if multiplied by another vector; scalar multiplication otherwise."""
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product.")
            
            return sum(a * b for a, b in zip(self.components, other.components))
        
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        
        else:
            raise TypeError("Multiplication is only supported with a scalar or another vector.")

    def __rmul__(self, other):
        """Handles scalar multiplication from the left (e.g., 3 * v1)."""
        return self.__mul__(other)

    def magnitude(self):
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        """Return the unit vector (normalized version)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))
