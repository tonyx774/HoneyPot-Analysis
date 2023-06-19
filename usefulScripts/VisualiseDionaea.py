import sqlite3
import sys
from time import strftime, localtime

arguements = sys.argv

conn = sqlite3.connect('dionaea.sqlite')


cursor = conn.cursor()

def displayHelpMenu():
        print("\nUsage")
        print("'-ip <ipaddress>'  - Display all attack data related to the given ip address")
        print("'-allip'           - Display attack data related to all ip addresses")
        print("'-md5'             - Display all submitted md5 hash of files along with the ip address they were received from")
        print("\n")

        
def displayHashesAndRelatedIPAddresses():
        cursor.execute("SELECT d.download_md5_hash, c.remote_host FROM downloads d JOIN connections c ON d.connection = c.connection;")
        rows = cursor.fetchall()
        for row in rows:
                print("MD5 Hash: ",row[0],"IP Address: ",row[1])

def displayIPAttackInfo(ipaddress):
        cursor.execute(f"SELECT c.remote_host, c.remote_port, c.connection_timestamp, c.connection_protocol, c.connection_type, d.download_md5_hash FROM connections AS c LEFT JOIN downloads AS d ON c.connection = d.connection WHERE c.remote_host = ?;",(ipaddress,))
        rows = cursor.fetchall()
        for row in rows:
                print("\nAttack info related to ",row[0])
                print("Attack Time: ",strftime('%Y-%m-%d %H:%M:%S', localtime(int(row[2]))))
                print("Remote Port: ",row[1])
                print("Connection Protocol: ",row[3])
                print("Connection Type: ",row[4])
                if(row[5] is not None):
                        print("This attack resulted in a binary being dropped, MD5 HASH: ",type(row[5]),"\n")

def displayAllIPAttackInfo():
 
    cursor.execute("SELECT DISTINCT remote_host FROM connections;")
    ip_addresses = cursor.fetchall()


    for ip_address in ip_addresses:
        ip = ip_address[0]
        cursor.execute("""
            SELECT c.remote_host, c.remote_port, c.connection_timestamp, c.connection_protocol, c.connection_type, d.download_md5_hash
            FROM connections AS c
            LEFT JOIN downloads AS d ON c.connection = d.connection
            WHERE c.remote_host = ?;
        """, (ip,))

   
        results = cursor.fetchall()

   
        
        for row in results:
                print("\nAttack info related to ",row[0])
                print("Attack Time: ",strftime('%Y-%m-%d %H:%M:%S', localtime(int(row[2]))))
                print("Remote Port: ",row[1])
                print("Connection Protocol: ",row[3])
                print("Connection Type: ",row[4])
                if(row[5] is not None):
                        print("This attack resulted in a binary being dropped, MD5 HASH: ",row[5],"\n")
        
def menu():

        if(len(sys.argv)<2):
                displayHelpMenu()
        elif(sys.argv[1] == "-ip"):
                displayIPAttackInfo(sys.argv[2])
        elif(sys.argv[1] == "-allip"):
                displayAllIPAttackInfo()
        elif(sys.argv[1] == "-md5"):
                displayHashesAndRelatedIPAddresses()
        else:
                displayHelpMenu()
menu()
cursor.close()
conn.close()
