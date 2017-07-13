# Tool for creating DNS traffic to test Safe Networking


import socket

# Some counters
counter = 0
good_domains = 0
bad_domains = 0


# Input file.  This code reads domain names from a .txt file and will attempt to resolve the IP Addr of the domain
f = open('c:\\temp\\bad_list.txt', 'r')

# Procssing of the file
for line in f:
    counter+=1
    try:
        addr1 = line.strip()
        addr2 = socket.gethostbyname(addr1)
        print (addr1, addr2)
        good_domains+=1
        
    except socket.gaierror:
        print ("cannot resolve hostname:", line)
        bad_domains+=1

# Wrap up
print ('Finished!')
print ('Total Domains tried:', counter)
print('Domains resolved:', good_domains)
print ('Blocked domains:', bad_domains)
print ('Done!')
