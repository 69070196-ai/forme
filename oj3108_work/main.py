"""promotion"""
a,b,c = map(int,(input()).split())
if a+b+c >= 3:
    print(int((a*25+b*40+c*55)*(1-0.1)))
else:
    print(int(a*25+b*40+c*55))
