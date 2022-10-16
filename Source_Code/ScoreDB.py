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
                (name,score) = line.split(",")
                self.scores.append((name,int(score)))
        else:
            self.scores.append(("---",0))
            lines.append("---,0")
            lines = "".join(lines)
            self.file.write(lines)

        self.file.close()


    def viewScores(self):
        scores = []
        for (name,score) in self.scores:
            score_str = f'{name} -- {score}'
            scores.append(score_str)
        return scores

    def addScore(self, score):
        (name,score) = score
        for i, (_,highscore) in enumerate(self.scores):
            if score > highscore:
                self.scores.insert(i,(name,score))
                break
        
        # recompile lines
        lines = []
        for (name,score) in self.scores:
            line = ""+name+","+str(score)+"\n"
            lines.append(line)

        # save to file
        self.file = open(self.filepath, 'w')
        lines = "".join(lines)
        self.file.write(lines)
        self.file.close()


            

def test():
    score1 = ScoreDB("test.txt")
    score2 = ScoreDB("highscores.txt")

    print(score1.scores[0])
    print(score2.scores[0])

    print(score2.viewScores())

    score2.addScore(("321",321))

    print(score2.viewScores())

    score1.file.close()
    score2.file.close()

#test()
