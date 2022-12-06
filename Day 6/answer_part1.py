

def contains_start_of_packet(buffer):
    packet_size = 14

    start = 0
    end = start + packet_size

    seq = []
    while end < len(buffer):
        temp = buffer[start:end]
        seq = [c for c in temp]
        check_set = set(seq)
        if len(check_set) == 14:
            print(temp)
            return end
        start += 1
        end += 1

f = open("D:\Documents\Advent of Code\Day 6\input.txt", "r")

lines = f.readlines()

result = 0


for line in lines:
    print(line)
    result = contains_start_of_packet(line)
    print(result)
    
print(result)
f.close()
