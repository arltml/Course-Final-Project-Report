class WineSample:
    """
    Represents single wine sample along with its chemcial properties
    """
    def __init__(self, features: dict, label: int = None):
        """
        Initialize a wine sample object
        """
        #Store chemical feature values for the wine sample
        self.features = features
        # Store the classification label (wine type)
        self.label = label
        
    def __str__(self):
        "Readable string representation of the wine sample."
        return f"WineSample(features ={self.features}, label={self.label})"
    def __eq__(self, other):
        """
        Comparison of two WineSample objects based on their features.
        """
        # Ensure comparison is only done between WineSample objects
        if not isinstance(other, WineSample):
            return False
        # Compare feature dictionaries
        return self.features == other.features
    
    def get_feature_vector(self):
        """
        features are returned as an immutable tuple
        """
        
        return tuple(self.features.values())