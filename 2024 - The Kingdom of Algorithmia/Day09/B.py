with open('in.txt') as f:
    content = f.read().splitlines()

brightness = [int(x) for x in content]
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
stamps = stamps[::-1]
count = [0 for _ in brightness]

def bfs(stamps, num):
    queue = [(num, 0)]

    while queue:
        num, count = queue.pop(0)
        if num == 0:
            return count
        for stamp in stamps:
            if num - stamp >= 0:
                queue.append((num-stamp, count+1))
                
for i,bright in enumerate(brightness):
    count[i] = bfs(stamps, bright)
    
print(sum(count))