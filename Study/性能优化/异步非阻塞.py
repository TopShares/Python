#对于多线程和多进程的缺点是在IO阻塞时会造成了线程和进程的浪费，所以异步IO回事首选：

# 异步非阻塞
# 【异步】, 回调
# 【非阻塞】,不等待 socket, 连接：发送数据；接收数据
# 【阻塞】: client = socket(); client.connect(ip, port)
# 【非阻塞】: client= socket(); client.setblocking(Flase); client.connect(ip, port)