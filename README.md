# Geomancy
Geomancy Algorithm
GEOMANCY is a form of divination based on the interpretation of figures or patterns drawn on the ground or other flat surface by means of sand or similar granular materials. The term is also used for the interpretation of geographic features([encyclopedia](https://www.encyclopedia.com/philosophy-and-religion/other-religious-beliefs-and-general-terms/miscellaneous-religion/geomancy))

[![(N|solid)](,https://upload.wikimedia.org/wikipedia/commons/a/ad/Geomantic_housechart.svg)]


[![(N|solid)](https://images.squarespace-cdn.com/content/v1/5859c8c603596e40874b984a/1578281775652-R7KQDME26QIAPP9IA9CE/ke17ZwdGBToddI8pDm48kB1nek-r9_fKmttojQdT0o1Zw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpxkmcCFddqaYICggqibSGl5UuaPblmPWdOXCh0RTRmTcvZAWJrb_MaYEBMvE196V5I/image1.png)]

### Geo
class Geo(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self)
 |  
 |  daughters(self)
 |      Combines neighbouring array components
 |      [(1, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 0), (1, 1, 0, 1)] => [(0, 1, 1, 1), (1, 0, 0, 1)]
 |  
 |  dots(self)
 |      Generate sixteen(16) random numbers between 1 and 16
 |      [3, 5, 14, 3, 7, 12, 11, 8, 4, 11, 10, 2, 3, 5, 6, 13]
 |  
 |  filia(self, array, n)
 |      split an array into n components
 |  
 |  judge(self)
 |      Combines neighbouring array components
 |       [(0, 1, 1, 1), (1, 0, 0, 1)] => (1, 1, 1, 0)
 |  
 |  mancy(self)
 |  
 |  mothers(self)
 |      split the array into n components
 |      [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1] => [(1, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 0), (1, 1, 0, 1)]
 |  
 |  sRes(self, array)
 |      Converts it to a binary array using the remainder of each random selection
 |      [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1]
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  session = 0
