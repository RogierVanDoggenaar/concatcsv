import hashlib

if __name__ == '__main__':
    with open("sample.csv", "a") as of:
        of.write("ID,sha1,brandID,url\n")
        i = 0
        for a in range(0, 10000000):
            i += 1
            url = "http://www.somelink.nl/%d" % i
            sha = hashlib.sha1(url.encode()).hexdigest()
            of.write("%d,%s,%d,%s\n" % (i, sha, i+100000, url))
        of.close()
