import pandas as pd 

thing = pd.read_csv("Resources/data/cities.csv")


html = thing.to_html()
print(html)

f = open("tablehtml.txt", "a")
f.write(html)
f.close()