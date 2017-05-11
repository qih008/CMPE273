# Qing Huang
# 02/10/2017
# CMPE173 Lab1

import psutil
import collections

socket = []
socket = psutil.net_connections()
result = []

print '"pid", "laddr", "raddr", "status"'

for i in range(len(socket)):
  if(socket[i].laddr != () and socket[i].raddr != ()):         # have socket connections
    temp = []
    temp.append(socket[i].pid)
    temp.append(socket[i].laddr[0]+"@"+str(socket[i].laddr[1]))
    temp.append(socket[i].raddr[0]+"@"+str(socket[i].raddr[1]))
    temp.append(socket[i].status)
    result.append(tuple(temp))

counts = collections.Counter(r[0] for r in result)
ans = sorted(result, key=lambda r:counts[r[0]], reverse=True)  # sort by pid frequency

for i in range(len(ans)):
  print '"'+str(ans[i][0])+'","'+ans[i][1]+'","'+ans[i][2]+'","'+ans[i][3]+'"'
