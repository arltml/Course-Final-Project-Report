import pandas as pd
from models.wine_dataset import WineDataset
from models.wine_sample import WineSample


def test_data_loading():
    # load csv file
    df = pd.read_csv("data/wine.csv")

    # make dataset and load data
    dataset = WineDataset()
    dataset.load_data(df)

    # check it's not empty
    assert len(dataset) > 0


def test_prediction():
    # load csv again
    df = pd.read_csv("data/wine.csv")

    # make dataset and load data
    dataset = WineDataset()
    dataset.load_data(df)

    # train model
    dataset.train_model()

    # example input values
    sample_features = {
        "alcohol": 13.0,
        "malic_acid": 2.0,
        "color_intensity": 5.0,
        "hue": 1.0
    }

    # create sample
    sample = WineSample(sample_features)

    # predict class
    prediction = dataset.predict(sample)

    # make sure prediction is valid
    assert prediction in [0, 1, 2]
