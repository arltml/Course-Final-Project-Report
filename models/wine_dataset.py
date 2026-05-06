import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
<<<<<<< HEAD
=======
import statistics
>>>>>>> ce76679 (rearrange structure of code)
from models.wine_sample import WineSample

class WineDataset:
    """
    Manages a collection of WineSample objects and performs classification and analysis
    """

    def __init__(self):
        """
        Initialize an empty wineDataset object
        """
        self.samples = []
        self.df = None
        self.model = None
    
    def load_data(self, df: pd.DataFrame):
        """
        Load a pandas DataFrame and convert each row into a WineSample object
        """
        self.df = df
        self.samples = []

        #Loop through each row in the DataFrame and create a WineSample object
        for _, row in df.iterrows():
            features = row.drop("target").to_dict()
            label = row["target"]

            self.samples.append(WineSample(features, label))
    
    def __len__(self):
        """
        Return the number of wine samples in the dataset
        """
        return len(self.samples)

    #Machine Learning section
    def train_model(self, k=3):
        """
        Train a K-Nearest Neighbors classifier using the dataset
        """
        if self.df is None:
            raise ValueError("Dataset not loaded")

        # X contains all feature columns, while y contains the target labels
        X = self.df.drop("target", axis=1)
        y = self.df["target"]

        #Create and train the KNN classifier
        self.model = KNeighborsClassifier(n_neighbors=k)
        self.model.fit(X, y)
    
    def predict(self, sample: WineSample):
        """
        Predict the wine class for a given WineSample object

        Returns:
            int: Predicted wine class
        """
        if self.model is None:
            raise ValueError("Model not trained")
        
        try:
            #the model expects a 2D list so the sample features are placed inside another list
            vector = [list(sample.features.values())]

            prediction = self.model.predict(vector)[0]
            return int(prediction)

        except Exception as e:
            raise RuntimeError(f"Prediction failed: {e}")
                               
    # Statistical Analysis Section

    def get_summary_stats(self):
        """
        Compute the mean value of each feature in the dataset

        returns:
            Dictionary where each key is a feature name and each value is the mean
        """
        if self.df is None:
            raise ValueError("Dataset not loaded")
        
        #Use dictionary comprehension to calculate the mean for every feature column
        return {
            col: self.df[col].mean()
<<<<<<< HEAD
            for col in self.df.columns if col != "target"
        }
=======
            for col in self.df.columns
            if col != "target"
        }

    def get_feature_ranges(self):
        """
        Compute the minimum and maximum values for each feature

        Returns:
            Dictionary in the formal {feature: (min,max)}
        """
        if self.df is None:
            raise ValueError("Dataset not loaded")
        
        #Store each features smallest and largest value as a tuple
        return{
            col: (self.df[col].min(), self.df[col].max())
            for col in self.df.columns
            if col != "target"
        }
    
    def get_class_distribution(self):
        """
        Count how many samples belonf to each wine class

        Returns:
            Dictionary in the format {class_label: count}
        """
        distribution = {}

        #Count each label by looping through the WineSample objects
        for sample in self.samples:
            label = sample.label

            if label in distribution:
                distribution[label] += 1
            else:
                distribution[label] = 1
        
        return distribution
    
    # Advanced Python features section

    def get_feature_matrix(self):
        """
        Returns the dataset as a list of lists
        """

        #Convert each WineSample objects feature dictionary into a list of values
        return [list(sample.features.values()) for sample in self.samples]

    def get_average_alcohol(self):
        """
        Compute the average alcohol value across all wine samples
        """

        if len(self.samples) == 0:
            raise ValueError("No samples available")
        
        #Use a generator expression to sum alcohol values without creating an extra list
        return sum(sample.features["alcohol"] for sample in self.samples) / len(self.samples)

    def normalize_features(self):
        """
        Normalize the feature columns using NumPy-style z-score normalization
        """
        if self.df is None:
            raise ValueError("Dataset not loaded")
        
        #Remove the target column because only numeric features should be normalized
        features = self.df.drop("target", axis=1)

        #Z-Score normalization: subtract the mean and divide by the standard deviation
        normalized = (features - features.mean()) / features.std()

        return normalized

    def feature_correlation(self):
        """
        Compute the correlation matrix for the dataset
        """
        if self.df is None:
            raise ValueError("Dataset not loaded")
        
        #Pandas corr() shows how strongly features are related to each other
        return self.df.corr()

    def describe_with_statistics_module(self):
        """
        Use the built-in statistics module to summarize the alcohol feature
        """
        if len(self.samples) == 0:
            raise ValueError("No samples available")
        
        #create a list of alcohol values from all WineSample objects
        alcohol_values = [sample.features["alcohol"] for sample in self.samples]

        return {
            "mean": statistics.mean(alcohol_values),
            "median": statistics.median(alcohol_values),
            "stdev": statistics.stdev(alcohol_values)
        }
    
    def pair_features_with_names(self):
        """
        Pair feature names with the values from the first sample
        """
        if self.df is None:
            raise ValueError("Dataset not loaded")
        
        if len(self.samples) == 0:
            raise ValueError("No samples available")
        
        #Get all column names except the final target column
        feature_names = list(self.df.columns[:-1])

        #Use the first sample as an example
        first_sample = self.samples[0]

        paired = []

        #Use zip to match feature names with values, and enumerate to add an index
        for i, (name, value) in enumerate(zip(feature_names, first_sample.features.values())):
            paired.append((i, name, value))
        
        return paired   
>>>>>>> ce76679 (rearrange structure of code)
