import sys,textwrap
import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
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
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

inp=sys.argv
inputdata=sys.argv[1]
srcip=sys.argv[2]
destip=sys.argv[3]
protocol='0011'
datasum=0000
a = srcip.split('.')
b = hex(int(a[0]))[2:].zfill(2) + hex(int(a[1]))[2:].zfill(2) + hex(int(a[2]))[2:].zfill(2) + hex(int(a[3]))[2:].zfill(2)
b = b.replace('0x', '')
s = b.upper()
a1 = destip.split('.')
b1 = hex(int(a1[0]))[2:].zfill(2) + hex(int(a1[1]))[2:].zfill(2) + hex(int(a1[2]))[2:].zfill(2) + hex(int(a1[3]))[2:].zfill(2)
b1 = b1.replace('0x', '')
d = b1.upper()
x = list(divide_chunks(inputdata, 4))  
srcp=x[0]
destp=x[1]
udplength=x[2]
checksum=x[3]
data1=[]
for i in range(4,len(x)):
 data1.append(x[i])
data1=''.join(data1)
#data=map(int, str(data1))
#print data
inputdata = str(data1) + '00'
inputdata = textwrap.wrap(inputdata,4)
#print inputdata
for i in range(len(inputdata)):
    inputdata[i] = int(inputdata[i],16)
#print inputdata
datasum=sum(inputdata)
datasum=hex(datasum)
datasum= datasum.replace('0x', '')
out=0
out=add_hex_mod(str(out),str(protocol))
m=len(s)-4
s1=s[:m]
s2=s[m:]
out=add_hex_mod(str(out),str(s1))
out=add_hex_mod(str(out),str(s2))
m=len(d)-4
d1=d[:m]
d2=d[m:]
out=add_hex_mod(str(out),str(d1))
out=add_hex_mod(str(out),str(d2))
out=add_hex_mod(str(out),str(srcp))
out=add_hex_mod(str(out),str(destp))
out=add_hex_mod(str(out),str(udplength))
out=add_hex_mod(str(out),str(udplength))
out=add_hex_mod(str(out),str(datasum))
complement= int(out, 16) ^ 0xFFFF
complement=hex(complement)[2:].zfill(4)
b=hashlib.sha256(data1.decode('hex')).hexdigest()
if(checksum==complement):
    i = int(srcp, 16)
    srcp=str(i)
    print srcp
    i = int(destp, 16)
    destp=str(i)
    print destp
    i = int(udplength, 16)
    udplength=str(i)
    print udplength
    print "0x"+complement
    print b
else:
    print"Invalid UDP segment"

