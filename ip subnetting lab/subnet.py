import json 
import sys
import math
import struct
import socket

def pad(l, content, width):
     l.extend([content] * (width - len(l)))
     return l

def next_power_of_2(x):  
    return 1 if x == 0 else 2**(x - 1).bit_length()

def bin_add(*args): 
	return bin(sum(int(x, 2) for x in args))[2:]

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def onelistmaker(n):
    listofones = [1] * n
    return listofones

def dec_to_addr(x):
	return socket.inet_ntoa(struct.pack('>L',x))

file = open(sys.argv[1],"r")
inputt = file.read()
inputt=json.loads(inputt)
# print inputt
network_addr=inputt["network_addr"] #192.168.128.0
subnets=inputt["subnets"] # {"1": 13, "2": 11, "3": 12}
netmask=inputt["netmask"] #255.255.224.0
# print network_addr
# print subnets
# print netmask
out_dict={}
subnetvalues=[]
subnet=dict()
nm=netmask.split('.')
each={}
na={}
sa={}
ea={}
thc={}
output_dict = {}
noz=0
count=0
csum=0
temp=0
for x in nm:
	if x =="255":
		noz=noz+0
	elif x=="0":
		noz=noz+8
	else:
		b=int(x)
		# print b
		b=bin(b)[2:].zfill(8)
		# print b
		b=len([ones for ones in b if ones=='0'])
		# print b
		noz=noz+b
# print noz
for x in subnets.values():
	subnetvalues.append(x)
# print len(subnetvalues)

# print subnetvalues
tempsubnetvalues={}
tempsubnetvalues=subnets.copy()
# print subnets
# print tempsubnetvalues
subnetvalues.sort()
subnetvalues.reverse()
round_list = []
round_key=[]
for i in subnetvalues:
	k=subnets.keys()[subnets.values().index(i)]
	# print k
	round_key.append(k)
	addval=i+2
	roundval=next_power_of_2(addval)
	round_list.append(roundval)
	subnets.pop(k)
round_dict= dict(zip(round_key, round_list))
# print subnets
csum=sum(round_list)
# print csum
noz2=int(math.pow(2,noz))
if csum > noz2:
	success = False
	output_dict["success"] = success
	print json.dumps(output_dict)
else:
	success = True
# print tempsubnetvalues
subnets=tempsubnetvalues.copy()
if success ==True:
	for i in subnetvalues:
		k=subnets.keys()[subnets.values().index(i)]
		subnets.pop(k)
		sub2=round_dict[k]
		if count==0:
			start_addr=network_addr
			count=count+1
			addbuf=start_addr
		else:
			endbuf=endbuf.split('.')
			d1 = bin(int(endbuf[0]))[2:].zfill(8) + bin(int(endbuf[1]))[2:].zfill(8) + bin(int(endbuf[2]))[2:].zfill(8) + bin(int(endbuf[3]))[2:].zfill(8)
			d2=bin(1)[2:].zfill(32)
			d=bin_add(d1,d2)
			d=int(d, 2)
			start_addr=dec_to_addr(d)
			check=start_addr.split('.')
			if int(check[3]) > 255:
				dif=int(check[3])-255
				check[3]=dif-1
				check[2]=int(check[2])+1
				ch= bin(int(check[0]))[2:].zfill(8) + bin(int(check[1]))[2:].zfill(8) + bin(int(check[2]))[2:].zfill(8) + bin(int(check[3]))[2:].zfill(8)
				ch=int(ch, 2)
				start_addr=dec_to_addr(ch)
			if int(check[2]) > 255:
				dif=int(check[2])-255
				check[2]=dif-1
				check[1]=int(check[1])+1
				ch= bin(int(check[0]))[2:].zfill(8) + bin(int(check[1]))[2:].zfill(8) + bin(int(check[2]))[2:].zfill(8) + bin(int(check[3]))[2:].zfill(8)
				ch=int(ch, 2)
				start_addr=dec_to_addr(ch)
			if int(check[1]) > 255:
				dif=int(check[1])-255
				check[1]=dif-1
				check[0]=int(check[0])+1
				ch= bin(int(check[0]))[2:].zfill(8) + bin(int(check[1]))[2:].zfill(8) + bin(int(check[2]))[2:].zfill(8) + bin(int(check[3]))[2:].zfill(8)
				ch=int(ch, 2)
				start_addr=dec_to_addr(ch)
			addbuf=start_addr
		addbuf=addbuf.split('.')
		s1 = bin(int(addbuf[0]))[2:].zfill(8) + bin(int(addbuf[1]))[2:].zfill(8) + bin(int(addbuf[2]))[2:].zfill(8) + bin(int(addbuf[3]))[2:].zfill(8)
		s2=bin(sub2-1)[2:].zfill(32)
		s=bin_add(s1,s2)
		s=int(s, 2)
		end_addr=dec_to_addr(s)
		check=end_addr.split('.')
		if int(check[3]) > 255:
			dif=int(check[3])-255
			check[3]=dif-1
			check[2]=int(check[2])+1
			ch= bin(int(check[0]))[2:].zfill(8) + bin(int(check[1]))[2:].zfill(8) + bin(int(check[2]))[2:].zfill(8) + bin(int(check[3]))[2:].zfill(8)
			ch=int(ch, 2)
			start_addr=dec_to_addr(ch)
		if int(check[2]) > 255:
			dif=int(check[2])-255
			check[2]=dif-1
			check[1]=int(check[1])+1
			ch= bin(int(check[0]))[2:].zfill(8) + bin(int(check[1]))[2:].zfill(8) + bin(int(check[2]))[2:].zfill(8) + bin(int(check[3]))[2:].zfill(8)
			ch=int(ch, 2)
			start_addr=dec_to_addr(ch)
		if int(check[1]) > 255:
			dif=int(check[1])-255
			check[1]=dif-1
			check[0]=int(check[0])+1
			ch= bin(int(check[0]))[2:].zfill(8) + bin(int(check[1]))[2:].zfill(8) + bin(int(check[2]))[2:].zfill(8) + bin(int(check[3]))[2:].zfill(8)
			ch=int(ch, 2)
			start_addr=dec_to_addr(ch)
		endbuf=end_addr
		# print start_addr
		# print end_addr
		q=0
		while sub2 > 2**q:
			q=q+1
		q=q-1
		minus=32-q
		# print minus
		l1=[]
		l2=[]
		l1=onelistmaker(minus-1)
		# print l1
		l1=pad(l1, 0, 32)
		str1 = ''.join(map(str, l1))
		# print str1
		str1=int(str1,2)
		# print str1
		# print socket.inet_ntoa(struct.pack('>L',str1))
		netmaskk=dec_to_addr(str1)
		total_host_count= sub2-2
		# print netmaskk
		na = {"network_addr":start_addr}
		sa = {"start_addr" :start_addr}
		ea = {"end_addr": end_addr}
		thc = {"total_host_count": total_host_count}
		dict1={}
		dict1["network_addr"]=start_addr
		dict1["netmask"]=netmaskk
		dict1["start_addr"]=start_addr
		dict1["end_addr"]=end_addr
		dict1["total_host_count"]=total_host_count
		# print dict1
		out_dict[k]=dict1
	# print out_dict
	output_dict["success"] = success
	output_dict["subnets"] = out_dict
	print json.dumps(output_dict)

