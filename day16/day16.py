# https://adventofcode.com/2021/day/16

file = open('input.txt', 'r')
hex2bits = {'0': [0,0,0,0],'1': [0,0,0,1],'2': [0,0,1,0],'3': [0,0,1,1],'4': [0,1,0,0],'5': [0,1,0,1],'6': [0,1,1,0],'7': [0,1,1,1],'8': [1,0,0,0],'9': [1,0,0,1],'A': [1,0,1,0],'B': [1,0,1,1],'C': [1,1,0,0],'D': [1,1,0,1],'E': [1,1,1,0],'F': [1,1,1,1]}
transmission = [bit for hex in file.readline().rstrip() for bit in hex2bits[hex]]

class Packet(object):
    def __init__(self):
        self.version = None
        self.type_id = None
        self.value = None
        self.children = []
    def __str__(self):
        return "Packet - version: " + str(self.version) + ", type id: " +  str(self.type_id) + ", value: " + str(self.value)
    
# prints the hierachy of the packets in a formatted fashion, for example:
# |---Packet - version: 6, type id: 0, value: 46
      # |---Packet - version: 0, type id: 0, value: 21
            # |---Packet - version: 0, type id: 4, value: 10
            # |---Packet - version: 6, type id: 4, value: 11
      # |---Packet - version: 4, type id: 0, value: 25
            # |---Packet - version: 7, type id: 4, value: 12
            # |---Packet - version: 0, type id: 4, value: 13
def print_packet_hierarchy(packets, indent = 0):
    for packet in packets:
        print('      '*(indent-1) + '|---' + str(packet))
        print_packet_hierarchy(packet.children, indent+1)
        
        
def bits2int(bits):
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out
    
    
def decode_next_packet(transmission):
    packet = Packet()
    packet.version = bits2int(transmission[0:3])
    packet.type_id = bits2int(transmission[3:6])
    idx = 6
    
    if packet.type_id == 4:
        # literal value
        value = []
        # decode value by looking at chunks for 5 bits
        while True:
            chunk = transmission[idx:idx+5] 
            value = value + chunk[1:]
            idx += 5
            if chunk[0] == 0:
                break
                
        packet.value = bits2int(value)
        transmission = transmission[idx:]
    else:
        # operator packet
        length_type_ID = transmission[idx]
        idx += 1 
        
        if length_type_ID == 0:
            # next 15 bits contain the total length in bits of subpackets in this packet
            length = bits2int(transmission[idx:idx+15])
            idx += 15
            
            block = transmission[idx:idx+length]
            packet.children = decode_packets(block)
            idx += length
            transmission = transmission[idx:]
            
        else:
            # next 11 bits is the number of subpackets immediately contained by this packet
            num_sub_packets = bits2int(transmission[idx:idx+11])
            idx += 11
            transmission = transmission[idx:]
            for i in range(num_sub_packets):
                child, transmission = decode_next_packet(transmission)
                packet.children.append(child)
                
    return packet, transmission

def decode_packets(transmission):
    packets = []
    while True:
        packet, transmission = decode_next_packet(transmission)
        packets.append(packet)
        if transmission.count(1) == 0:
            break
    return packets


def count_versions(packets):
    count = 0
    for packet in packets:
        count += packet.version
        count += count_versions(packet.children)
    return count


def evaluate(packet):
    if packet.value is None:
        for child in packet.children:
            evaluate(child)
        
        if packet.type_id == 0:
            packet.value = sum([child.value for child in packet.children])
        if packet.type_id == 1:
            packet.value = 1
            for child in packet.children:
                packet.value *= child.value
        if packet.type_id == 2:
            packet.value = min([child.value for child in packet.children])
        if packet.type_id == 3:
            packet.value = max([child.value for child in packet.children])
        if packet.type_id == 5:
            if packet.children[0].value > packet.children[1].value:
                packet.value = 1
            else:
                packet.value = 0
        if packet.type_id == 6:
            if packet.children[0].value < packet.children[1].value:
                packet.value = 1
            else:
                packet.value = 0
        if packet.type_id == 7:
            if packet.children[0].value == packet.children[1].value:
                packet.value = 1
            else:
                packet.value = 0
    return packet.value


packets = decode_packets(transmission)
#print_packet_hierarchy(packets, 1)

print('Result part 1: ', count_versions(packets))
print('Result part 2: ', evaluate(packets[0]))
