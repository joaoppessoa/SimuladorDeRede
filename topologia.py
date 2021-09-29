from Computador import Computador
from grafo import Grafo
from Switch import Switch

c1 = Computador('C1', '192.168.0.12', '77:87:01:0C:1E:A6')
c2 = Computador('C2', '192.168.0.11', '01:7F:6C:29:3A:31')
c3 = Computador('C3', '192.168.0.10', '41:12:96:A0:E2:7E')
c4 = Computador('C4', '10.0.0.10', 'E8:51:28:27:93:92')
c5 = Computador('C5', '10.0.0.11', 'A3:38:6A:69:21:E9')
c6 = Computador('C6', '10.0.0.12', '68:FC:A5:88:DD:9F')
c7 = Computador('C7', '192.168.1.12', '5B:6E:F0:09:33:19')
c8 = Computador('C8', '192.168.1.11', 'E7:30:81:9E:99:A3')
c9 = Computador('C9', '192.168.1.10', '13:84:69:E4:01:59')

S1 = Switch('S1', '192.168.10.10', '38:A4:65:A6:61:5C', 4)
S2 = Switch('S2', '192.168.10.11', '38:A4:65:A6:61:A7', 16)
S3 = Switch('S3', '192.168.10.12', '38:A4:65:A6:61:10', 8)
