import pandas as pd
from models.wine_dataset import WineDataset
from models.wine_sample import WineSample

def test_data_loading():
    df = pd.read_csv("data/wine.csv")
    dataset = WineDataset()
    dataset.load_data(df)

    assert len(dataset) > 0

def test_prediction():
    df = pd.read_csv("data/wine.csv")
    dataset = WineDataset()
    dataset.load_data(df)
    dataset.train_model()

    sample_features = {
        "alcohol": 13.0,
        "malic_acid": 2.0,
        "color_intensity": 5.0,
        "hue": 1.0
    }

    sample = WineSample(sample_features)
    prediction = dataset.predict(sample)

    assert prediction in [0, 1, 2]
