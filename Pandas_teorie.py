import pandas as pd

s = pd.Series([10,20,30],name="Scor")
df = pd.DataFrame({
    "nume":["ana","ion","mihai"],
    "varsta":[20,21,22],
    "nota":[9.5,4.4,6.6]
})

df=pd.read_csv("C:\\Users\\Pop\\Desktop\\python\\StudentPerformanceFactors.csv")
#print(df.head(4))
#print(df.columns)
#print(df.dtypes)
#print(df.info())
#print(df.describe(include="all"))
#print(df[df["Hours_Studied"].isin([10])])
#print(df.loc[2,"Hours_Studied"])
#print(df.iloc[2:3,1:3])
if (df["Hours_Studied"] == 0).any():
    print(df.loc[df["Hours_Studied"] == 0, "Hours_Studied"])
print(df.loc[df["Hours_Studied"] == 0])
df["Hours_Studied"]=df["Hours_Studied"].fillna(df["Hours_Studied"].mean())
print(df.Hours_Studied)


