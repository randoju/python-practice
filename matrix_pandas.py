import pandas as pd

p = [[1, 5, 9],
     [3, 6, 11],
     [4, 7, 13]]

x = 11

# Create a DataFrame from the list
df = pd.DataFrame(p)


# Iterate over each cell in the DataFrame
for index, value in df.stack().items():
    # If the value equals x, print its position
    if value == x:
        print("Element found at position", index)
