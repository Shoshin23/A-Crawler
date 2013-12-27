What is it?
=========

A simple web-crawler writtin in Python. 


Usage
======

``` 
python crawler.py -l <url>
```
Now this will fetch links for the target URL only. 

```
python crawler.py -d<n> <url>

python crawler.py <url>
```
Where n is the depth that you want to traverse. 
In the 2nd case, when just the target URL is provided, the default depth of traversal is 10.


```
python crawler.py -h 
```
Throws up the help section for you to see commands that you can use. 

<b> References: </b>

<a href="http://en.wikipedia.org/wiki/Web_crawler">Wikipedia</a>
