
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!!!注意：1. 实际代理地址XXX.XXX.XXX.XXX:XX将取代MyProxy，
//            在修改脚本时，将脚本中要返回代理地址的地方用MyProxy填写!!!
//         2. 编辑脚本的时候一定要小心，一点点错误就会导致浏览器不能正常上网!!!
//         3. 请详细阅读代理自动配置脚本的有关知识，安装包已经提供了!!!
//         4. 注释符号是:   /* 被注释掉的 */   或两个斜杠//
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


function FindProxyForURL(url, host)
{
	url = url.toLowerCase();
	host = host.toLowerCase();

//不经过代理，直通的网站 
	if(isPlainHostName(host))  return "DIRECT";

//似乎不能使用dnsDomainIs(host,".cn")
//来准确判定是否在中国，不能得到正确的结果(如www.cnn.com)
	else if(dnsDomainIs(host,".cn"))  return "DIRECT";
	else if(shExpMatch(host, "*bbs.*"))  return "DIRECT";

//摘录自hustonline.net
	else if(
	(shExpMatch(host, "*edu.cn")) || (shExpMatch(host, "*hustonline.net")) || (shExpMatch(host, "*eistar.net")) || 
	(shExpMatch(host, "*sina.com.cn")) || (shExpMatch(host, "*sohu.com")) || (shExpMatch(host, "*222.20.*")) || 
	(shExpMatch(host, "*202.112.20.*")) || (shExpMatch(host, "*162.105.31.250*")) || (shExpMatch(host, "*202.120.61.1*")) || 
	(shExpMatch(host, "*202.114.*")) || (shExpMatch(host, "*218.197.*")) || (shExpMatch(host, "*smth.org")) || 
	(shExpMatch(host, "*hustnews.com")) || (shExpMatch(host, "*future.org.cn")) || (shExpMatch(host, "*luojia.net")) || 
	(shExpMatch(host, "*stuhome.net")) || (shExpMatch(host, "*ytht.net")) || (shExpMatch(host, "*smth.org")) || 
	(shExpMatch(host, "*ehust.net")) || (shExpMatch(host, "*hustgroup.com")) || (shExpMatch(host, "*5qzone.net")) || 
	(shExpMatch(host, "*zuiwan.net")) || (shExpMatch(host, "*byhh.net")) || (shExpMatch(host, "*ac.cn")) || 
	(shExpMatch(host, "*hustzs.cn")) || (shExpMatch(host, "*cas.cn")) || (shExpMatch(host, "*5qblog.net")) || 
	(shExpMatch(host, "*5qblog.com")) || (shExpMatch(host, "*cdut.net")) || (shExpMatch(host, "*my0635.net")) || 
	(shExpMatch(host, "*neupioneer.com")) || (shExpMatch(host, "*hustshop.net")) || (shExpMatch(host, "*baidu.com")) || 
	(shExpMatch(host, "*univchina.org")) || (shExpMatch(host, "*kyxk.net")) || (shExpMatch(host, "*hust.net.cn")) || 
	(shExpMatch(host, "*hust.com.cn")) || (shExpMatch(host, "*bingyan.net")) || (shExpMatch(host, "*stuhome.com"))
			)  return "DIRECT";
			
	else if(shExpMatch(host, "*.163.*"))  return "DIRECT";
	else if(shExpMatch(host, "*.263.*"))  return "DIRECT";
	else if(shExpMatch(host, "*.blogchina.com"))  return "DIRECT";
	else if(shExpMatch(host, "*.listeningexpress.*"))  return "DIRECT";
	

//拦截讨厌的网站
	else if(shExpMatch(url, "*.3721.*")) return "PROXY 0.0.0.0:3421";	

//不经过代理，直通的IP地址段(摘录自proxy expert)
	else if(isInNet(host,"61.28.0.0", "255.255.240.0"))  return "DIRECT";
	else if(isInNet(host,"61.48.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"61.128.0.0", "255.192.0.0"))  return "DIRECT";
	else if(isInNet(host,"61.232.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"61.236.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"61.240.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"63.84.162.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"63.240.81.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"63.240.90.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"63.240.94.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"63.240.105.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"64.124.183.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"64.124.183.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"128.84.158.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"132.174.1.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"132.174.11.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"137.189.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"140.98.193.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"140.98.194.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"140.113.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"143.89.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"144.214.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"147.8.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"152.101.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"152.104.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"158.132.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"158.182.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"159.226.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"161.207.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"162.105.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"165.193.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"166.111.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"167.139.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"167.216.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"168.160.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"192.58.150.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"192.80.71.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"192.84.75.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"192.86.104.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"192.195.245.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"193.123.78.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"193.194.158.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"194.130.252.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"195.22.150.0", "255.255.254.0"))  return "DIRECT";
	else if(isInNet(host,"198.112.160.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"199.4.155.0", "255.255.254.0"))  return "DIRECT";
	else if(isInNet(host,"199.98.88.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"199.164.217.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"202.4.128.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"202.38.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"202.38.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"202.40.192.0", "255.255.240.0"))  return "DIRECT";
	else if(isInNet(host,"202.45.32.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"202.75.64.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"202.84.16.0", "255.255.254.0"))  return "DIRECT";
	else if(isInNet(host,"202.95.0.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"202.96.0.0", "255.240.0.0"))  return "DIRECT";
	else if(isInNet(host,"202.112.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"202.120.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"202.122.32.0", "255.255.240.0"))  return "DIRECT";
	else if(isInNet(host,"202.127.0.0", "255.255.192.0"))  return "DIRECT";
	else if(isInNet(host,"202.127.128.0", "255.255.128.0"))  return "DIRECT";
	else if(isInNet(host,"202.130.0.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"202.130.224.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"202.131.208.0", "255.255.240.0"))  return "DIRECT";
	else if(isInNet(host,"202.192.0.0", "255.240.0.0"))  return "DIRECT";
	else if(isInNet(host,"203.81.16.0", "255.255.240.0"))  return "DIRECT";
	else if(isInNet(host,"203.87.224.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"203.93.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"203.128.128.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"203.192.0.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"203.207.64.0", "255.255.192.0"))  return "DIRECT";
	else if(isInNet(host,"203.207.128.0", "255.255.128.0"))  return "DIRECT";
	else if(isInNet(host,"203.208.0.0", "255.255.240.0"))  return "DIRECT";
	else if(isInNet(host,"203.212.0.0", "255.255.240.0"))  return "DIRECT";
	else if(isInNet(host,"204.179.122.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"205.243.231.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"207.189.64.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"208.215.179.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"210.5.0.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"210.12.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.14.160.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"210.14.192.0", "255.255.192.0"))  return "DIRECT";
	else if(isInNet(host,"210.15.0.0", "255.255.128.0"))  return "DIRECT";
	else if(isInNet(host,"210.15.128.0", "255.255.192.0"))  return "DIRECT";
	else if(isInNet(host,"210.21.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.22.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.25.0.0", "255.255.128.0"))  return "DIRECT";
	else if(isInNet(host,"210.25.128.0", "255.255.192.0"))  return "DIRECT";
	else if(isInNet(host,"210.26.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.28.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.32.0.0", "255.240.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.51.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.52.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.72.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.76.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.78.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.82.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"210.192.96.0", "255.255.224.0"))  return "DIRECT";
	else if(isInNet(host,"211.64.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"211.80.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"211.96.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"211.136.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"211.144.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"211.160.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"216.33.115.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"216.39.32.0", "255.255.255.0"))  return "DIRECT";
	else if(isInNet(host,"216.52.36.0", "255.255.254.0"))  return "DIRECT";
	else if(isInNet(host,"218.0.0.0", "255.224.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.56.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.64.0.0", "255.224.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.96.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.104.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.108.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.192.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.200.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.204.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"218.240.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"219.72.0.0", "255.255.0.0"))  return "DIRECT";
	else if(isInNet(host,"219.128.0.0", "255.224.0.0"))  return "DIRECT";
	else if(isInNet(host,"219.216.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"219.224.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"219.232.0.0", "255.248.0.0"))  return "DIRECT";
	else if(isInNet(host,"219.242.0.0", "255.254.0.0"))  return "DIRECT";
	else if(isInNet(host,"219.244.0.0", "255.252.0.0"))  return "DIRECT";
	else if(isInNet(host,"220.192.0.0", "255.240.0.0"))  return "DIRECT";
	else if(isInNet(host,"10.0.0.0", "255.0.0.0"))  return "DIRECT";
	else if(isInNet(host,"172.16.0.0", "255.240.0.0"))  return "DIRECT";
	else if(isInNet(host,"192.168.100.0", "255.255.0.0"))  return "DIRECT";
	
	else return "PROXY MyProxy";
}

