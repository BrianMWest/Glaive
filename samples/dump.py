import glaive

glaive.init()

for packet in glaive.stream():
    print(packet)

glaive.close()
