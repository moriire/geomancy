# Geomancy
###Geomancy Algorithm

GEOMANCY is a form of divination based on the interpretation of figures or patterns drawn on the ground or other flat surface by means of sand or similar granular materials. The term is also used for the interpretation of geographic features([encyclopedia](https://www.encyclopedia.com/philosophy-and-religion/other-religious-beliefs-and-general-terms/miscellaneous-religion/geomancy))

[![(N|solid)](,https://upload.wikimedia.org/wikipedia/commons/a/ad/Geomantic_housechart.svg)]


[![(N|solid)](https://images.squarespace-cdn.com/content/v1/5859c8c603596e40874b984a/1578281775652-R7KQDME26QIAPP9IA9CE/ke17ZwdGBToddI8pDm48kB1nek-r9_fKmttojQdT0o1Zw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpxkmcCFddqaYICggqibSGl5UuaPblmPWdOXCh0RTRmTcvZAWJrb_MaYEBMvE196V5I/image1.png)]
```sh
from geomancy import Geo
geo = Geo()
```
```sh
geo.mancy()
Random Samples(16)=>[2, 11, 12, 7, 2, 7, 14, 1, 16, 7, 4, 1, 9, 3, 12, 6]
Cleaned data => [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1]
mothers => [[1, 1, 0, 1], [1, 0, 1, 1], [0, 0, 0, 1], [0, 1, 0, 1]]
daughters => [[0, 1, 0, 1], [1, 0, 0, 0]]
Judge => [1, 1, 0, 0]
```
## Geo(builtins.object)
###  dots()
 ```sh
 geo.dots() #Generate sixteen(16) random numbers between 1 and 16
 [3, 5, 14, 3, 7, 12, 11, 8, 4, 11, 10, 2, 3, 5, 6, 13]
```
###  mothers()
 ```sh
 geo.mothers() #split the array into 4 components
 [(1, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 0), (1, 1, 0, 1)] => [(0, 1, 1, 1), (1, 0, 0, 1)]
```
###  daughters()
 ```sh
 geo.daughters() ###Combines neighbouring array components into 2
 [(1, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 0), (1, 1, 0, 1)] => [(0, 1, 1, 1), (1, 0, 0, 1)]
```
###  judge()
 ```sh
 geo.judge() #Combines neighbouring array components
  [(0, 1, 1, 1), (1, 0, 0, 1)] => (1, 1, 1, 0)
```
