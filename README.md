# Language

This is a simple programming language decoder. you can decode html and css(style sheet). More simple than Beautiful Soup and work smoothly for heavy data. It will give you data in the format of list, tuple and dictinory so it is simple to use and analyse.

#Html parsing begining...👇
first import HyperTextMarkup from language pip

>from Language import HyperTextMarkup

create an object and give the html to the object

>MyObj = HyperTextMarkup(html)

now get a tag. This will give a list of all tags you entered.

>MyObj.get("a")
["<a href="https://youtube.com/c/abamtech">",<a href="https://techabam.blogspot.com">","<a href="https://techabam.000webhostapp.com">"]

Now get the contents by the contents. This will give you the contents in the a order

>MyObj.contents
["abam youtube channel","abam blog","abam site"]

more informations will come in our site, blog or youtube channel please visit..

#css decoding begining...👇

first import styleSheet class from Languages lib and create an object.

>from Languages import styleSheet
>MyObj = styleSheet(data)

Site: https://techabam.000webhostapp.com
Youtube Channe: https://youtube.com/c/abamtech
Blog: https://techabam.blogspot.com

#Whats new? (v1.4.0)

1.You can directly open a file that contains your data.

>MyObj = Languages.class("C://Your_file")

2.Now you can decode stylesheet(css) using the stylesheet class. And simply go through the styles of a page

>MyObj = Languages.styleSheet(data)

3. Stability and performance improoved. simply go through big data. more functions added.


version 1.5.0 comeing soon. with more features.

#previous versions:
 V 1.0.0 =>dont have new features like styleSheet etc. dont recommend
 
 V 1.1.0 =>Deleted due to the unstability
 
 V 1.2.0 =>Not recommended dont have new features
 
 v 1.4.0 =>Recommended tested all new features availabale.

abam