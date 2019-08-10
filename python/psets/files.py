
def minimumTime(numOfSubFiles, files):
    print(files)
    # WRITE YOUR CODE HERE
    if numOfSubFiles == 0 or numOfSubFiles == 1:
        return 1
    
    if numOfSubFiles == 2:
        return min(files[0], files[1])
    
    mem = [files[0], min(files[0], files[1]]
    for i,file in enumerate(files):
        curr = min(file, files[i-1])
        mem[0] = mem[1]
        mem[1] = curr
        
    return mem[1]

if __name__ == '__main__':
    print(minimumTime(4, [20, 4, 8, 2]))