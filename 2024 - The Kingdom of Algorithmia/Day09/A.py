with open('in.txt') as f:
    content = f.read().splitlines()

brightness = [int(x) for x in content]
stamps = [10,5,3,1]
count = [0 for _ in brightness]

for i,bright in enumerate(brightness):
    for stamp in stamps:
        while bright-stamp >= 0:
            bright = bright-stamp
            count[i] += 1
print(sum(count))