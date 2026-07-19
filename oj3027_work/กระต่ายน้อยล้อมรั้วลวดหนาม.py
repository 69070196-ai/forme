"""คำนวณล้อมรั้ว"""
spike = input().split()
spike_p = int(input())
w,l,h=spike
w = int(w)
l = int(l)
h = int(h)
d = ((w*2)+(l*2))*h
price = d *spike_p
print(d)
print(price)
