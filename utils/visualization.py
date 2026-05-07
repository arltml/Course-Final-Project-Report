import matplotlib.pyplot as plt


def plot_feature_distribution(df, feature):
    """
    Create histogram of features
    """
    if feature not in df.columns:
        raise ValueError(f"{feature} not found in dataset.")

    plt.figure()
    plt.hist(df[feature], bins=20)
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()


def plot_scatter(df, feature_x, feature_y):
    """
    Create scatter plot
    """
    if feature_x not in df.columns or feature_y not in df.columns:
        raise ValueError("Invalid feature names.")

    plt.figure()
    plt.scatter(df[feature_x], df[feature_y])
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.title(f"{feature_x} vs {feature_y}")
    plt.show()
