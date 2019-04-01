import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

############### Read a CSV file
app = pd.read_csv('googleplaystore.csv')
dfRaw = pd.DataFrame(app)
i = dfRaw[(dfRaw.App == 'Life Made WI-Fi Touchscreen Photo Frame')].index
tempApp = dfRaw[(dfRaw.App != 'Life Made WI-Fi Touchscreen Photo Frame')]
dfApp = pd.DataFrame(tempApp)
app.drop(i)
dfApp.dropna()
def konversi(a):
    try:
        value = float(a[1:-1])
        suffix = a[-1:]

        if suffix == 'M':
            value = value * 1024 * 1024
        elif suffix == 'K':
            value = value * 1024
    except ValueError:
        value = 0
    return value
dfApp['Size'] = dfApp['Size'].apply(konversi)
# print(dfApp.info())
dfApp['Installs']=dfApp['Installs'].str[:-1]
dfApp['Installs']=dfApp['Installs'].str.replace(",","")
dfApp["Installs"] = pd.to_numeric(dfApp["Installs"], errors='coerce')
dfApp = dfApp.dropna(subset=["Installs"])
dfApp["Installs"] =dfApp["Installs"].astype('float64')
# print(dfApp['Installs'])
dfApp['Price']=dfApp['Price'].str.replace("$","")
dfApp["Price"] = pd.to_numeric(dfApp["Price"], errors='coerce')
dfApp = dfApp.dropna(subset=["Price"])
dfApp["Price"] =dfApp["Price"].astype('float64')
dfApp['Rating'] = dfApp['Rating'].fillna(0)
# print(dfApp['Price'][0])

############### View the data
# print(dfApp)
# print(dfApp['Size'])
# print(dfApp.columns)            # shows all the columns
# print(len(dfApp.columns))       # shows the sums of them (reference)
# print(dfApp.sort_values(by='Category'))
# print(dfApp.sort_values(by='Last Updated'))
# print(dfApp.iloc[10472])
# print(len(dfApp))
# print(len(dfApp))
# print(dfApp.sort_values(by='Category'))

############### Take any necessary variables
# tempCat = dfApp.pivot_table(index='Category', columns='Installs')
# print(tempCat)
# groupCat = dfApp.groupby('Category')
# category = groupCat.get_group('ART_AND_DESIGN')
# print(category)
aName = []
category = []
rating = []
review = []
size = []
installs = []
aType = []
price = []
cRating = []
genre = []
lastUpdate = []
currentVer = []
androidVer = []
for check in (dfApp.values):
    aName.append(check[0])
    category.append(check[1])
    rating.append(check[2])
    review.append(check[3])
    size.append(check[4])
    installs.append(check[5])
    aType.append(check[6])
    price.append(check[7])
    cRating.append(check[8])
    genre.append(check[9])
    lastUpdate.append(check[10])
    currentVer.append(check[11])
    androidVer.append(check[12])
dfName = pd.DataFrame(aName, columns = ['App Name'])
dfCatRaw = pd.DataFrame(category, columns = ['Category'])
dfRatRaw = pd.DataFrame(rating, columns = ['Rating'])
dfRevRaw = pd.DataFrame(review, columns = ['Review'])
dfSizeRaw = pd.DataFrame(size, columns = ['Size'])
dfInstRaw = pd.DataFrame(installs, columns = ['Installs'])
dfTypeRaw = pd.DataFrame(aType, columns = ['Type'])
dfPriceRaw = pd.DataFrame(price, columns = ['Price'])
dfCRatRaw = pd.DataFrame(cRating, columns = ['Content Rating'])
dfGenreRaw = pd.DataFrame(genre, columns = ['Genre'])
dfLURaw = pd.DataFrame(lastUpdate, columns = ['Last Update'])
dfCVRaw = pd.DataFrame(currentVer, columns = ['Current Ver'])
dfAVRaw = pd.DataFrame(androidVer, columns = ['Android Ver'])

############### sort anything
# Category
catName = dfCatRaw
catName.drop_duplicates(keep = 'first', inplace = True)
nCategory = catName.values
dfCategory = pd.DataFrame(nCategory, columns = ['Category'])
# print(dfCategory)
# Rating
ratNumber = dfRatRaw
ratNumber.drop_duplicates(keep = 'first', inplace = True)
nRating = ratNumber.values
dfRating = pd.DataFrame(nRating, columns = ['Rating'])
# print(dfRating)
# Installs
sinstalls = dfInstRaw
sinstalls.drop_duplicates(keep = 'first', inplace = True)
ninstalls = sinstalls.values
dfinstalls = pd.DataFrame(ninstalls, columns = ['Installs'])
# print(dfinstalls)
# Content Rating
cRatNumber = dfCRatRaw
cRatNumber.drop_duplicates(keep = 'first', inplace = True)
nCRating = cRatNumber.values
dfCRating = pd.DataFrame(nCRating, columns = ['Content Rating'])
# print(dfCRating)
# Genre
sGenre = dfGenreRaw
sGenre.drop_duplicates(keep = 'first', inplace = True)
nGenre = sGenre.values
dfGenre = pd.DataFrame(nGenre, columns = ['Genre'])
# print(dfGenre)
# Type
sType = dfTypeRaw
sType.drop_duplicates(keep = 'first', inplace = True)
nType = sType.values
dfType = pd.DataFrame(nType, columns = ['Type'])
# Price
sPrice = dfPriceRaw
sPrice.drop_duplicates(keep = 'first', inplace = True)
nPrice = sPrice.values
dfPrice = pd.DataFrame(nPrice, columns = ['Price'])

############### 1. Total App in Each Category
# print(len(dfApp[(dfApp['Category'] == dfCategory['Category'][2])]))
sumsCatAll = []
for x in range(len(dfCategory)):
    sumsCatAll.append(len(dfApp[(dfApp['Category'] == dfCategory['Category'][x])]))
listCategory = []
for x in (dfCategory.values):
    listCategory.append(x[0])
catSumList = []
for x in range(len(listCategory)):
    catSumList.append((listCategory[x],sumsCatAll[x]))
# print(catSumList)
dfSumsCatAll = pd.DataFrame(catSumList, columns = ['Category','Total App'])
# print(dfSumsCatAll)
totalApp1Category = dfSumsCatAll.sort_values(by = ['Total App'], ascending = True)
# print(totalApp1Category)

############### Each Category Based on Content Rating
# print(len(dfApp[(dfApp['Category'] == dfCategory['Category'][0]) & (dfApp['Content Rating'] == dfCRating['Content Rating'][3])]))
listCRating = []
for x in (dfCRating.values):
    listCRating.append(x[0])
# print(listCRating)
cRE = []
cRTeen = []
cRE10 = []
cRM = []
cRA = []
cRU = []
for x in range(len(dfCategory)):
    cRE.append(len(dfApp[(dfApp['Category'] == dfCategory['Category'][x]) & (dfApp['Content Rating'] == dfCRating['Content Rating'][0])]))
for x in range(len(dfCategory)):
    cRTeen.append(len(dfApp[(dfApp['Category'] == dfCategory['Category'][x]) & (dfApp['Content Rating'] == dfCRating['Content Rating'][1])]))
for x in range(len(dfCategory)):
    cRE10.append(len(dfApp[(dfApp['Category'] == dfCategory['Category'][x]) & (dfApp['Content Rating'] == dfCRating['Content Rating'][2])]))
for x in range(len(dfCategory)):
    cRM.append(len(dfApp[(dfApp['Category'] == dfCategory['Category'][x]) & (dfApp['Content Rating'] == dfCRating['Content Rating'][3])]))
for x in range(len(dfCategory)):
    cRA.append(len(dfApp[(dfApp['Category'] == dfCategory['Category'][x]) & (dfApp['Content Rating'] == dfCRating['Content Rating'][4])]))
for x in range(len(dfCategory)):
    cRU.append(len(dfApp[(dfApp['Category'] == dfCategory['Category'][x]) & (dfApp['Content Rating'] == dfCRating['Content Rating'][5])]))
catCRSumList = []
for x in range(len(listCategory)):
    catCRSumList.append((listCategory[x],cRE[x],cRTeen[x],cRE10[x],cRM[x],cRA[x],cRU[x]))
columnsCatCR = ['Category']
for x in (dfCRating.values):
    columnsCatCR.append(x[0])
dfSumsCatCR = pd.DataFrame(catCRSumList, columns = columnsCatCR)
# print(dfSumsCatAll)

############### Total App Each Content Rating
sumsCRatAll = []
for x in range(len(dfCRating)):
    sumsCRatAll.append(len(dfApp[(dfApp['Content Rating'] == dfCRating['Content Rating'][x])]))
cRatSumList = []
for x in range(len(listCRating)):
    cRatSumList.append((listCRating[x],sumsCRatAll[x]))
dfSumsCRatAll = pd.DataFrame(cRatSumList, columns = ['Content Rating','Total App'])
totalApp1CRating = dfSumsCRatAll.sort_values(by = ['Total App'], ascending = True)
# print(totalApp1CRating)

############### Total App Each Type
sumsTypeAll = []
for x in range(len(dfType)):
    sumsTypeAll.append(len(dfApp[(dfApp['Type'] == dfType['Type'][x])]))
listType = []
for x in (dfType.values):
    listType.append(x[0])
typeSumList = []
for x in range(len(listType)):
    typeSumList.append((listType[x],sumsTypeAll[x]))
dfSumsTypeAll = pd.DataFrame(typeSumList, columns = ['Type','Total App'])
totalApp1Type = dfSumsTypeAll.sort_values(by = ['Total App'], ascending = True)
# print(totalApp1Type)

############### Total App Each Price
sumsPriceAll = []
for x in range(len(dfPrice)):
    sumsPriceAll.append(len(dfApp[(dfApp['Price'] == dfPrice['Price'][x])]))
listPrice = []
# print(listPrice)
for x in (dfPrice.values):
    listPrice.append(x[0])
priceSumList = []
for x in range(len(listPrice)):
    priceSumList.append((listPrice[x],sumsPriceAll[x]))
dfSumsPriceAll = pd.DataFrame(priceSumList, columns = ['Price','Total App'])
totalApp1Price = dfSumsPriceAll.sort_values(by = ['Price'], ascending = True)
# print(totalApp1Price)

############### Machine-Learning
####### Preparation for model training
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
### 2. bases : Size and Type
# print(dfApp[(dfApp['Type'] == dfType['Type'][0])])

####### Split & Train any possible bases: train 90% & test 10%
from sklearn.model_selection import train_test_split
####### 1. Split train first plan
xtrain1,xtest1,ytrain1,ytest1 = train_test_split(
    dfApp[['Size']],
    dfApp['Rating'],
    test_size = .1
)
# print(xtrain1)
# print(ytrain1)
####### 1. Target: Rating based on: Size
from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
## 1. train model
model1.fit(xtrain1, ytrain1)

## 1. Accuracy
print(model1.score(xtest1,ytest1))

## 1. prediction
print(model1.predict(xtest1))

## 1. plot actual data
fig1 = plt.figure('Rating Based on App Sizes', figsize = (30,65))
plt.plot(
    dfApp['Size'],
    dfApp['Rating'],
    marker = 'o',
    color = 'g'
)
## 1. plot prediction data
plt.plot(
    dfApp['Size'],
    model1.predict(dfApp[['Size']]),
    marker = 'o',
    color = 'r'
)
# plt.show()