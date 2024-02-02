# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
    
    def handle_endtag(self, tag):
        print("End   :", tag)
    
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])


N = int(input())


html_code = ""
for _ in range(N):
    html_code += input()

parser = MyHTMLParser()
parser.feed(html_code)
