# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *

'''
import httplib2

def getnetwords():
    url = 'http://www.mieliestronk.com/corncob_lowercase.txt'
    http = httplib2.Http()
    content = http.request(url)[1]
    content = str(content, 'utf-8')
    wlist = content.split()
    for j in range(len(wlist)):
    #    print(word, end=' ')
        wlist[j] += '\n'
    with open('wurds.txt', 'w') as f:
        f.writelines(wlist)
        f.close()
    return wlist
#'''

def getwords():
    wlist = []
    #getnetwords()

    with open('wurds.txt', 'r') as f:
        wlist = f.readlines()
        f.close()
    for j in range(len(wlist)):
        word = wlist[j]
        word = word.strip()
        word = word.lower()
        wlist[j] = word
        #print(word, end=' ')
    return wlist

def find(search, needle):
    k = 0
    needle_len = len(needle)
    for j in range(len(search)):
        if search[j] == needle[k]:
            k += 1
        if k == needle_len:
            return True

    return False

def mysort(e):
    return len(e)

def match(comp, wlist, count):
    textout = ''
    textlst = []
    scomp = sorted(comp)
    for wd in wlist:
        swd = sorted(wd)
        search = ''.join(scomp[0:count])
        needle = ''.join(swd)
        if count >= len(wd) > 2:
            if find(search, needle):
                textlst.append(''.join(wd))
    textlst.sort(reverse=True, key=mysort)
    textout = '\n'.join(textlst)
    text.delete('1.0', 'end')
    text.insert(INSERT, textout)


def domatch():
    search = search_text.get()
    search = search.lower()
    match(search, wlist, len(search))
    scrl.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    win = Tk()
    #win.geometry('250x450')
    win.winfo_toplevel().title('Anagram Search')
    search_text = StringVar()

    frame = Frame(win)
    myfont = ("Consolas", 20, "normal")

    lframe = LabelFrame(frame)
    #label = Label(lframe, text='Word Search ')
    entry = Entry(lframe, width=14, font=myfont, textvariable=search_text)
    button = Button(lframe, text='Search', command=domatch)
    entry.bind('<Return>', lambda event: domatch())

    tframe = LabelFrame(frame)
    #label.pack(side=LEFT)
    entry.pack(side=LEFT, fill=BOTH)
    button.pack(side=LEFT, fill=BOTH)

    scrl = Scrollbar(tframe, orient='vertical')
    text = Text(tframe, width=17, height=15, font=myfont, yscrollcommand=scrl.set)
    scrl.config(command=text.yview)

    text.pack(side=LEFT, fill=BOTH)
    scrl.pack(side=RIGHT)
    lframe.pack(side=TOP, fill=BOTH)
    tframe.pack(side=BOTTOM, fill=BOTH)

    frame.pack()

    wlist = getwords()

    win.mainloop()


