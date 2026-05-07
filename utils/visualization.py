import matplotlib.pyplot as plt


def plot_feature_distribution(df, feature):
    # plots a histogram 

    # check if the feature exists in the dataframe
    if feature not in df.columns:
        raise ValueError(f"{feature} not found in dataset.")

    # creates a new figure
    plt.figure()

    # 20 bins
    plt.hist(df[feature], bins=20)

    # add title and labels
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")

    # display the plot
    plt.show()


def plot_scatter(df, feature_x, feature_y):
    # plots  scatter plot 

    # check both features
    if feature_x not in df.columns or feature_y not in df.columns:
        raise ValueError("Invalid feature names.")

    # create a figure
    plt.figure()

    # plot scatter points
    plt.scatter(df[feature_x], df[feature_y])

    # axes
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)

    # titles
    plt.title(f"{feature_x} vs {feature_y}")

    # display the plot
    plt.show()
