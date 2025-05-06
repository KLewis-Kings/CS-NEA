class Levels():
    def __init__(self):
        self.levelData = []
    def initLevels(self):
        #open levelfiles
        #for fname in levelfiles
        # split of newline 
        # call loadlevel witn filename
        #append to level data
        fname="lvl1.txt"
        m1=self.loadLevel(fname)
        self.levelData.append(m1)
    def getLevel(self, level):
        return self.levelData[level]
    
    def loadLevel(self, fname):
        fname=open("lvl1.txt","r")
        l=[]
        for lines in fname:
            lines.strip("\n")
            lines=lines.replace("_", " ")
            l.append(lines)
        fname.close()
        return l