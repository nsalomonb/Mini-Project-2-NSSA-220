node1IP = "192.168.100.1"
node2IP = "192.168.100.2"
node3IP = "192.168.200.1"
node4IP = "192.168.200.2"

node1 = []
node2 = []
node3 = []
node4 = []
node5 = []

def compute(L) :
	print 'called compute function in compute_metrics.py'
	computing(L)

def parse(file_name, L):
    file = open(file_name, "r")
    for line in file:
        L.append(line.split())
    file.close()
	
def computing(L):
	reqsent = 0;
	reqrecieved = 0;
	
	repsent = 0;
	reprecieved = 0;
	
	for i in range(len(L)):
		print L[i][10]
	
		if L[i][8] == "reply":
			if L[i][2] == "192.168.100.1":
				repsent = repsent + 1
			elif L[i][3] == "192.168.100.1":
				reprecieved = reprecieved + 1
				
		if L[i][8] == "request":
			if L[i][2] == "192.168.100.1":
				reqsent = reqsent + 1
			elif L[i][3] == "192.168.100.1":
				reqrecieved = reqrecieved + 1
				
	
	print "Requests Sent: " + str(reqsent)
	print "Requests Recieved: " + str(reqrecieved)
	
	print "Replies Sent: " + str(repsent)
	print "Replies Recieved: " + str(reprecieved)

def numRequestBytesSent(ip):
    total = 0
    for n1 in node1:
        if n1[2] == ip and n1[8] == "request":
            total = total + int(n1[5])
    for n2 in node2:
        if n2[2] == ip and n1[8] == "request":
            total = total + int(n2[5])
    for n3 in node3:
        if n3[2] == ip and n1[8] == "request":
            total = total + int(n3[5])
    for n4 in node4:
        if n4[2] == ip and n1[8] == "request":
            total = total + int(n4[5])
    return total

def numRequestBytesRecieved(ip):
    total = 0
    for n1 in node1:
        if n1[3] == ip and n1[8] == "request":
            total = total + int(n1[5])
    for n2 in node2:
        if n2[3] == ip and n1[8] == "request":
            total = total + int(n2[5])
    for n3 in node3:
        if n3[3] == ip and n1[8] == "request":
            total = total + int(n3[5])
    for n4 in node4:
        if n4[3] == ip and n1[8] == "request":
            total = total + int(n4[5])
    return total

def numRequestDataSent(ip):
    total = 0
    for n1 in node1:
        if n1[2] == ip and n1[8] == "request":
            total = total + int(n1[5]) - 42
    for n2 in node2:
        if n2[2] == ip and n1[8] == "request":
            total = total + int(n2[5]) - 42
    for n3 in node3:
        if n3[2] == ip and n1[8] == "request":
            total = total + int(n3[5]) - 42
    for n4 in node4:
        if n4[2] == ip and n1[8] == "request":
            total = total + int(n4[5]) - 42
    return total

def numRequestDataRecieved(ip):
    total = 0
    for n1 in node1:
        if n1[3] == ip and n1[8] == "request":
            total = total + int(n1[5]) - 42
    for n2 in node2:
        if n2[3] == ip and n1[8] == "request":
            total = total + int(n2[5]) - 42
    for n3 in node3:
        if n3[3] == ip and n1[8] == "request":
            total = total + int(n3[5]) - 42
    for n4 in node4:
        if n4[3] == ip and n1[8] == "request":
            total = total + int(n4[5]) - 42
    return total

# Logic for Time Metrics

def rtt(node, ip):
    total = 0
    count = 0
    for i in range(0, len(node1), 2):
        if node[i][2] == ip and node[i][8] == "request":
            total = total + (float(node[i + 1][1]) - float(node[i][1]))
            count = count + 1
    return total / count

def echoRequestThroughput(node, ip):
    total = 0
    for i in range(0, len(node), 2):
        total = total + (float(node[i + 1][1]) - float(node[i][1]))
    return numRequestBytesSent(ip)/total

def echoRequestGoodput(node, ip):
    total = 0
    for i in range(0, len(node), 2):
        total = total + (float(node[i + 1][1]) - float(node[i][1]))
    return numRequestDataSent(ip)/total

parse("Node1_filtered.txt", node1)
parse("Node2_filtered.txt", node2)
parse("Node3_filtered.txt", node3)
parse("Node4_filtered.txt", node4)
parse("Node5_filtered.txt", node5)

		
# Node 1 - 192.168.100.1
# Node 2 - 192.168.100.2
# Node 3 - 192.168.200.1
# Node 4 - 192.168.200.2
# Node 5 - 192.168.100.254
		
	
	
# 0 - Number
# 1 - Time
# 2 - Src IP
# 3 - Dest IP
# 4 - ICMP
# 5 - Length
# 6 - Echo                | Destination
# 7 - Ping                | Unreachable
# 8 - reply/request       | (Host
# 9 - ID                  | Unreachable)
#10 - SEQ
#11 - TTL
#12 - (reply/request
#13 - in
#14 - Reply Time


	
