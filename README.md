# Language

This is a simple html decoder. you can decode html and view through the html page. More simple than Beautiful Soup .
first import HyperTextMarkup from language pip

>>from Language import HyperTextMarkup

create an object and give the html to the object

>>MyObj = HyperTextMarkup(html)

now get a tag. This will give a list of all tags you entered.

>>MyObj.get("a")
["<a href="https://youtube.com/c/abamtech">",<a href="https://techabam.blogspot.com">","<a href="https://techabam.000webhostapp.com">"]

Now get the contents by the contents. This will give you the contents in the a order

>>MyObj.contents
["abam youtube channel","abam blog","abam site"]

more informations will come in our site, blog or youtube channel please visit..

Site: https://techabam.000webhostapp.com
Youtube Channe: https://youtube.com/c/abamtech
Blog: https://techabam.blogspot.com
