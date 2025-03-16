import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))  # 0.0.0.0 erlaubt Verbindungen von überall
server.listen(2)

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

print("Server läuft...")

while True:
    client, addr = server.accept()
    clients.append(client)
    print(f"Neue Verbindung: {addr}")

    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            broadcast(msg, client)
        except:
            break

    print(f"Verbindung getrennt: {addr}")
    clients.remove(client)
    client.close()
#reh98734rznm8974t5c23689c542t24ct3hj89m7ct243j59h78c4t253hm897ct234rhm9687cr4t23h181444444444444444441414141414141414141414141414d3z8u34h892cm234m7823c4f8734hx34wh34xdf934fxh7893x4fh798x4fw3h798fx439h8f43hm789fx4hm9fw43f34hmw79xfh789fh894f3xcmh94f3ch9349cfh8w3c93w49834xfhyhyhhxfhx5h89x54h8x54h78x54h78x54wh789x45hw798n243h7243jky42k8x24h2xf34hm8x4fhm89x4hm89x439hm24x3fh9824x3fhbz894h48yfhy4fy43fk22k34xh34xbhx34b9mz8,xyf4m839z,fxhyzxzyc8byxchbrzbr9erzfiufuifzonu9i3320913um8342xmj234x78342hmnx439oayK,4yym4h4ffcz7b9yxfn9f43xym873494f3f4g978f452gnf245xxf8493xf4x4f282xf4x2f4xf2n74fx29f2x9n8xf2n92fx4xf242xf42xf42xfnm42xf4nm2xf42fxn43xng3x4789h3m2f389hxhnm2fx82nm4x2x42f4xn2x4f9n2x4372x4fn9f2x74f2fx4xf24nmxf24xf24xg4f2xfxf97xf4x4f2m2fmxf27hh2xf2f2xfxm2x252xm2x52x52x5mm2xh5fm8927hx5fx85hmf79m5xf8f2549zx5hfxy5m4298fxhy2389fg2y894y7d43h38472hfdhfhzw3fq3uwefdg83q489zrq37z8r93783rq4z983reqzrq3e4z34r7qq3487934qr3489u34r879h4r383d24h34d709q3f   hq3eriq3efoiq3feio3fqeffhhhfhfuhfq0mx438rz18342xrzm0xt2431u8m034xqr89z0243xzqz0234xz8m0zx348298