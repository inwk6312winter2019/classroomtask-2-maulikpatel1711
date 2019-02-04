import calc
for a in ipcalc.network('192.168.0.1/24'):
    print str(a)
    subnet = ipcalc.Network('255.255.255.0/24')
    print str(subnet.network())
print str(subnet.netmask())
    '192.168.0.1' in Network('192.168.0.1/24')
  def __str__(self):
          ipformat = ""
          for ips in self.ip:
              ipformat = ipformat + str(ips) +  "."
myip = ipaddress([192,168,1,1],[255,255,255,0])
print(myip)

