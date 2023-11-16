import pandas as pd
from ydata_profiling import ProfileReport


# ficticious cyclomatic complexity
def fictitious_function(x, y, z):
    if x > 0:
        print("X is positive.")
        if y > 0:
            print("Y is positive.")
            if z > 0:
                print("Z is positive.")
        elif y < 0:
            print("Y is non-positive.")
    elif x < 0:
        print("X is negative.")
    else:
        print("X is zero.")


def process_data(csv_file):
    # Load data from a CSV file or DataFrame
    dataFile = pd.read_csv(csv_file)

    # Data processing logic
    # ...proc
    return dataFile


df = process_data('train-make fake a subset of cyrosleep - MAKE FAKE CHILD OF CYRO.CSV')
print(df.head(10))
print(df.describe())

df['Age'].plot()

print(df["HomePlanet"].fillna("Missing", inplace=True))

profile = ProfileReport(df, title="Pandas Profiling Report")

profile.to_file("d:/python-projects/myfile.html")

print("Please find the updated file at d:/python-projects/myfile.html")

fictitious_function(1, 1, 1)

