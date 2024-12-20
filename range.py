import socket

def scan_ports(sex):
    print("scanning", sex)
    ports = [21, 22, 23, 53, 80, 443, 3389, 6697]
    for scanport in ports:  
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.1)
            result = client.connect_ex((sex, scanport))
            
            if result == 0:
                print(f"{sex}:{scanport}: Open")
                with open(f"range.txt", "a") as file:
                    file.write(f"{sex}:{scanport} \n")
         
               
        except socket.error:
            print(f"Port {scanport}: Error occurred")

    client.close()


def main():
    sex = input("ip range:")
    parts = sex.split('.')

    range_1 = int(parts[0])
    range_2 = int(parts[1])
    range_3 = int(parts[2])
    range_4 = int(parts[3])
    range_3_3 = 0
    range_4_4 = 0
    while True:
        range_4 += 1
        joined = f"{str(range_1)}.{str(range_2)}.{str(range_3)}.{str(range_4)}"
        scan_ports(joined)
        if range_4 >= 255:   ## this code is actual garbage 
            joined_2 = f"{str(range_1)}.{str(range_2)}.{str(range_3)}.{str(range_4_4)}"
            range_4 = 0
            range_3 += 1
            range_4_4 += 1
            scan_ports(joined_2)  ## i am actually ashamed of how much of a cluster fuck this is 
            if range_3 >= 255:
                if range_3 == 255:
                    exit()
                joined_3 = f"{str(range_1)}.{str(range_2)}.{str(range_3_3)}.{str(range_4_4)}"
                range_3 = 0
                range_3_3 += 1 ##genuinely embarrassing
                scan_ports(joined_3)
                
    
main()