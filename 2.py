import pyshorteners
s=pyshorteners.Shortener()
link=input("Enter link : ")
print(s.tinyurl.short(link))
