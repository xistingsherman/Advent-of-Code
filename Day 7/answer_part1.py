class Dir(object):
    def __init__(self,parent=None,name=None):
        self.parent = parent
        self.name = name
        self.children = []
        self.size = 0

class File(object):
    def __init__(self,parent=None,name=None,size=0):
        self.parent = parent
        self.name = name
        self.size = size

def postOrder(f, root):
    if root:
        for each in root.children:
            if isinstance(each, Dir):
                postOrder(f,each)
            root.size += each.size
        f.write(root.name + " " + str(root.size) + "\n")
        print(root.name + " " + str(root.size))

def main():
    f = open("D:\Documents\Advent of Code\Day 7\main.txt", "r")

    lines = f.readlines()

    root = Dir(None, "/")

    current_node = root

    add_files = True

    for line in lines:
        line = line.strip()

        if "$ cd" in line:
            add_files = False
            temp = line.split(" ")
            new_parent_name = temp[2]
            new_parent_name = new_parent_name.strip()
            #print(ascii(new_parent_name))
            if new_parent_name == ".." and current_node.parent:
                #print("this is")
                current_node = current_node.parent #update this
                #print(current_node.parent.name) #this is not being reached yet
            else:
                for each in current_node.children:
                    #print(current_node.name + " > " + each.name)
                    if isinstance(each,Dir) and each.name == new_parent_name:
                        current_node = each
                        #print("hello")
                        break
        elif line == "$ ls":
            add_files = True
        
        elif add_files == True:
            x, name = line.split(" ")
            x = x.strip()
            name = name.strip()
            #print(name)

            if "dir" in x:
                new_dir = Dir(current_node, name)
                current_node.children.append(new_dir)
                #print(current_node.name + " > " + new_dir.name)
            else:
                #print(x)
                new_file = File(current_node,name,int(x))
                current_node.children.append(new_file)

    output = open("output.txt", "a")
    postOrder(output, root)
    output.close()
    
    f.close()

    parse_results = open("D:\Documents\Advent of Code\output.txt", "r")

    total = 0
    listy = []
    for line in parse_results:
        line = line.strip()
        dir_name, dir_size = line.split(" ")
        dir_size = int(dir_size)
        if dir_size <= 100000:
            total += dir_size
    
    print(total)

if __name__ == "__main__":
    main()