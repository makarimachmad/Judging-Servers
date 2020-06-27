# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 17:19:35 2020

@author: makarim, afif, fathur
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

case = input()
case = int(case)

n_server = 0
n_beli = 0

for i in range(case):
    S, N = input().split()
    S = int(S)
    N = int(N)
    Pi = input().split()
    
    Pi = [int(Pi) for Pi in Pi]
    
    minim = min(Pi)
    indexmin = Pi.index(minim)
    
    Cost = minim
    
    
    server_left = 0
    server_right = 0
    
    if N > 2:
        
        if Pi[indexmin-1] <= Pi[indexmin+1]:
            Cost = Cost + Pi[indexmin-1]
            server_right = indexmin
            server_left = indexmin-1
        elif Pi[indexmin-1] >= Pi[indexmin+1]:
            Cost = Cost + Pi[indexmin+1]
            server_right = indexmin+1
            server_left = indexmin  
            
            
        for y in range(N-3):
            if Pi[server_left-1] >= Pi[server_right+1]:
                Cost = Cost + Pi[server_left-1]
                server_left = server_left-1
                print(server_left,server_right)
            elif Pi[server_left-1] <= Pi[server_right+1]:
                Cost = Cost + Pi[server_right+1]
                server_right = server_right+1
                print(server_left,server_right)
       
        
                
#    jumlah = 0
#    for j in range(n_beli-1):
#        jumlah = jumlah + sort_harga[j]
#    
    print ("Case {}:".format(i+1),Cost)
