
def test():
    t = "test lee"
    print(t)
    t = t + "!!!"
    print(t)
    print(t[1:3]) # es
    print(len(t))
    print(t.find("l")) # 5
    print(t.count("l")) # 1

    print(t.replace("l", "z") ) # test zee!!!
    print(t.upper())
    print(t.lower())

    # ---------- ---------- ---------- ----------
    print("---------- ---------- ---------- ----------")
    num = [1,2,3]
    print(type(num))
    print(num[0])
    num.append(4)
    print(num)
    num += [6]
    print(num)
    num.insert(4, 5)
    print(num)
    next = [7,8]
    num.extend(next)
    print(num)

    print(num.index(2))
    print(num.count(3))
    num.reverse()
    print(num)
    num.sort()
    print(num)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
