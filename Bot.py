from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException

scrapper = Scrapper(category="ALL", print_err_trace=False)

data = scrapper.getProxies()
path = input("Enter the path of the .txt file on which to write the proxies: ")
f = open(path, "a")

for item in data.proxies:
    proxy = '{}:{}\n'.format(item.ip, item.port)
    f.write(proxy)

f.close()

# Print the size of proxies scrapped
print("Total Proxies")
print(data.len)

# Print the Category of proxy from which you scrapped
print("Category of the Proxy")
print(data.category)