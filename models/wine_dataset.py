import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from wine_sample import WineSample

class WineDataset:
    """
    Manage collection of WineSample objects and performs classification
    """

    def __init__(self):
        """
        Initialize an empty dataset
        """
        self.samples = []
        self.df = None
        self.model = None

    def load_data(self, df: pd.DataFrame):
        """
        Loads dataset from Pandas DataFrame and creates WineSample Objects
        """
        self.df = df
        self.samples = []
        #Loop for creating dataset with rows
        for _, row in df.iterrows():
            features = row.drop("target").to_dict()
            label = row["target"]
            sample = WineSample(features, label)
            self.samples.append(sample)
