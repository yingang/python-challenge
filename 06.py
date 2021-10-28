import sys
import zipfile

def next(zf, id, comments):
    filename = id + '.txt'

    if filename not in zf.namelist():
        return None, None

    info = zf.getinfo(filename)
    comment = info.comment.decode('utf-8')

    words = zf.open(filename).read().decode('utf-8')
    print(words)
    if words == "Yes. Divide by two and keep going.":
        return str(int(id)//2), comment
    else:
        return words.split()[-1], comment

if __name__ == "__main__":
    zf = zipfile.ZipFile('channel.zip', 'r')
    start = '90052'
    comments = ''
    while len(start) > 0:
        start, comment = next(zf, start, comments)
        if start == None:
            break
        comments += comment
    print(comments)
