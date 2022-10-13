import os

class ScoreDB:

    def __init__(self,filepath="highscores.txt"):
        self.filepath = filepath

        # Create the highscore file if it does not exist yet
        # Initialize highscore to zero
        if not os.path.exists(filepath):
            self.file = open(filepath, 'w')
            self.file.write("---,0")
            self.file.close()

        # If the file exists, load the information

        self.file = open(filepath, 'r+')
        record = self.file.readline()
        record = record.split(",")
        self.highscore = (record[0],int(record[1]))


    def viewScores(self):
        ret = []
        for lines in self.file.readlines():
            record = lines.split(",")
            ret.append((record[0],int(record[1])))
        return ret

def main():
    score1 = ScoreDB("test.txt")
    score2 = ScoreDB("highscores.txt")

    print(score1.highscore)
    print(score2.highscore)

    print(score2.viewScores())

    score1.file.close()
    score2.file.close()

main()
