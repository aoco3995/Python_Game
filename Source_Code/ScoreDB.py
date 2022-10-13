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
        self.scores = []
        lines = self.file.readlines()
        if len(lines) > 0:
            for line in lines:
                record = line.split(",")
                self.scores.append((record[0],int(record[1])))
        else:
            self.scores.append(("---",0))
            lines.append("---,0")
            lines = "".join(lines)
            self.file.write(lines)

        self.file.close()


    def viewScores(self):
        return self.scores

    def addScore(self, score):
        for i, highscores in enumerate(self.scores):
            if score[1] > highscores[1]:
                self.scores.insert(i,score)
                break
        
        # recompile lines
        lines = []
        for score in self.scores:
            line = ""+score[0]+","+str(score[1])+"\n"
            lines.append(line)

        # save to file
        self.file = open(self.filepath, 'w')
        lines = "".join(lines)
        self.file.write(lines)
        self.file.close()


            

def main():
    score1 = ScoreDB("test.txt")
    score2 = ScoreDB("highscores.txt")

    print(score1.scores[0])
    print(score2.scores[0])

    print(score2.viewScores())

    score2.addScore(("mid",200))

    print(score2.viewScores())

    score1.file.close()
    score2.file.close()

main()
