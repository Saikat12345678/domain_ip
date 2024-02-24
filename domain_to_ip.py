import socket 
import pyfiglet
from urllib.parse import urlparse

text = pyfiglet.figlet_format("Domain-IP")
print(text)

class Domain:  
    def internet_protocol(self):
        try:
        
            mn = """ 1.Domain \n 2.Domain_with Link \n 3.exit()"""
            print(mn)  
            
            while True:
                user_choice = input("Enter Choice(1-3): ")
                    
                if user_choice == '1':
                    user_domain = input("Enter Domain: /")
                    domains = socket.gethostbyname(user_domain)
                    print("Your IP: ", domains)
                        
                elif user_choice == '2':
                    user_urls = input("Enter Urls/WithDomain: /")
                    url = urlparse(user_urls).hostname
                    domain = socket.gethostbyname(url)
                    print("Your IP: " ,domain)
                    
                elif user_choice == '3':
                    print()
                    print("Thanks for using!")
                    print()
                    break
                    
                
                else:
                    print("Enter Correct Value")
        except KeyboardInterrupt:
            print("Opps! Something Wrong!")
        except TypeError:
            print("Opps! Something Wrong!")  
        except socket.gaierror:
            print("Opps! Something Wrong!")  
        except Exception as e:
            print("Opps! Something Wrong!")
                   

domain_to_ip = Domain()

domain_to_ip.internet_protocol()            