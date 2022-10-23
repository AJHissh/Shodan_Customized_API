import shodan

api = shodan.Shodan('api-key')

def shodan_connect():
    x = True  
    while x is True:
        
        ip_add = input('enter ip: ')
        try:
            info = api.host(ip_add)
            print(info)
        except:
            print('No information for that IP')            
        finally:
            cont_or_exit = str(input('type yes to continue or press any key to exit: '))
            print(cont_or_exit)
            if cont_or_exit in ['Yes', 'yes', 'YES']:
                x = True
            elif cont_or_exit in ['No', 'no', 'NO']:
                x = False
                exit()
            
shodan_connect()
        
    
