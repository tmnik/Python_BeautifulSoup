# Extract the href= values from the anchor tags,
# scan for a tag that is in a particular position from the top
# and follow that link, repeat the process a number of times,
# and report the last name you find.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

n = input('Enter count: ')
n = int(n)
r = input('Enter position: ')
r = int(r)

for i in range(n):
    if i == 0:
        url = input('Enter - ')
    else:
        url = adr[r]

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    adr = list()
    consts = list()

    tags = soup('a')
    for tag in tags:
        name = tag.get('href', None)
        const = tag.contents[0]
        adr.append(name)
        consts.append(const)
print(adr[r])
print(consts[r])
