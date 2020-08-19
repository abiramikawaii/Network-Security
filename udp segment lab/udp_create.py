import sys,textwrap
def pad(l, content, width):
     l.extend([content] * (width - len(l)))
     return l

def add_hex_mod(hexstr1, hexstr2):
     pt = str.split(hexstr1)
     sk = str.split(hexstr2)
     for x in range(0, len(pt)):
         hex1 = '0x' + pt[x]
         hex2 = '0x' + sk[x]
         out= hex((int(hex1, 16) + int(hex2, 16)) % (2 ** 64))
     out= out.replace('0x', '')
     out=out.strip( 'L' )
     while(len(out)>4):
         m=len(out)-4
         ex=out[:m]
         out=out[m:]
         out=add_hex_mod(str(out),str(ex))
     return out       
l=len(sys.argv)
inp=sys.argv
srcip=sys.argv[1] #192.168.56.1
srcp=int(sys.argv[2]) #4444
destip=sys.argv[3] #192.168.56.2
destp=int(sys.argv[4]) #9999
data1=sys.argv[5] #3132333435
#print data1
data2=data1
num=len(str(data1))#neww
#print num
udplength=(num/2 + 8)#neww
# print udplength
data1=data1.decode("hex")
#print data1
datasum=0000
protocol=hex(17)
protocol=protocol[2:]
protocol=protocol.zfill(4)
a = srcip.split('.')
b = hex(int(a[0]))[2:].zfill(2) + hex(int(a[1]))[2:].zfill(2) + hex(int(a[2]))[2:].zfill(2) + hex(int(a[3]))[2:].zfill(2)
b = b.replace('0x', '')
s = b.upper()
a1 = destip.split('.')
b1 = hex(int(a1[0]))[2:].zfill(2) + hex(int(a1[1]))[2:].zfill(2) + hex(int(a1[2]))[2:].zfill(2) + hex(int(a1[3]))[2:].zfill(2)
b1 = b1.replace('0x', '')
d = b1.upper()
inputdata=data1+chr(0)##newww
inputdata=inputdata.encode('hex')
srcp=hex(srcp)
srcp=srcp[2:].zfill(4)
#print srcp
destp=hex(destp)
destp=destp[2:].zfill(4)
#print destp
udplength=hex(udplength)
udplength=udplength[2:]
udplength=udplength.zfill(4)
#print inputdata
inputdata = textwrap.wrap(inputdata,4)
for i in range(len(inputdata)):
    datasum=add_hex_mod(str(datasum),inputdata[i])
out=0
out=add_hex_mod(str(out),str(protocol))
m=len(s)-4
s1=s[:m]
#print s1
s2=s[m:]
#print s2
out=add_hex_mod(str(out),str(s1))
out=add_hex_mod(str(out),str(s2))
m=len(d)-4
d1=d[:m]
#print d1
d2=d[m:]  
#print d2
out=add_hex_mod(str(out),str(d1))
out=add_hex_mod(str(out),str(d2))
out=add_hex_mod(str(out),str(srcp))
out=add_hex_mod(str(out),str(destp))
out=add_hex_mod(str(out),str(udplength))
out=add_hex_mod(str(out),str(udplength))
out=add_hex_mod(str(out),str(datasum))
#print out
complement= int(out, 16) ^ 0xFFFF
complement=(hex(complement)[2:]).zfill(4)
#print complement
output=srcp+destp+udplength+str(complement)+str(data2)
print output