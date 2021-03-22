# Proxy-List-Scrapper
Proxy List Scrapper from various websites. They gives the free proxies for temporary use.

# Usage

- Install Proxy-List-Scrapper
  `pip install Proxy-List-Scrapper`
  _Make sure you have installed the requests and urllib3 in python_

- In import add
  `from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException`
  
- After that simply create an object of Scrapper class as "scrapper"
  `scrapper = Scrapper(category=Category, print_err_trace=False)`
  
- Here Your need to specify category defined as below:
  |Type|Link|
  |--|--|
  |SSL|'https://www.sslproxies.org/'|
  |GOOGLE|'https://www.google-proxy.net/'|
  |ANANY|'https://free-proxy-list.net/anonymous-proxy.html'|
  |UK|'https://free-proxy-list.net/uk-proxy.html'|
  |US|'https://www.us-proxy.org/'|
  |NEW|'https://free-proxy-list.net/'|
  |SPYS_ME|'http://spys.me/proxy.txt'|
  |PROXYSCRAPE|'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all'|
  |PROXYNOVA|'https://www.proxynova.com/proxy-server-list/'|
  |PROXYLIST_DOWNLOAD_HTTP|'https://www.proxy-list.download/HTTP'|
  |PROXYLIST_DOWNLOAD_HTTPS|'https://www.proxy-list.download/HTTPS'|
  |PROXYLIST_DOWNLOAD_SOCKS4|'https://www.proxy-list.download/SOCKS4'|
  |PROXYLIST_DOWNLOAD_SOCKS5|'https://www.proxy-list.download/SOCKS5'|
  |ALL|'ALL'|
  
- Get ALL Proxies According to your Choice
  `data = scrapper.getProxies()`
  
- @proxies is the list of Proxy Class which has actual proxy.
- @len is the count of total proxies in @proxies.
- @category is the category of proxies defined above.

