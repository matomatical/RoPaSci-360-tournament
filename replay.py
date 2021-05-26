import sys
import collections

from console import fg, bg, fx
from console.utils import clear, wait_key



def main():
    # load logfile
    try:
        path = sys.argv[1]
        with open(path) as f:
            data = f.readlines()
    except:
        print("usage: replay <path to valid logfile>", sys.stderr)
        sys.exit(1)

    # parse into turns and compute board pictures
    game = Game()
    slides = [game.display(message=f"replaying {path}")]
    prev_action = None
    for line in data:
        if line.startswith("turn"):
            number, player, action = parse_turn(line.strip())
            if player == "upper":
                prev_action = action
            else:
                game.update(upper_action=prev_action, lower_action=action)
                slides.append(game.display(message=f"turn {number}"))
        else:
            slides.append(f"{slides[-1]}\n{line}")
    
    # replay game
    i = 0
    while True:
        clear()
        print(slides[i])
        print("j: prev   k: next   q: quit")
        k = wait_key()
        if k == "j":
            i = max(0, i - 1)
        elif k == "k":
            i = min(i + 1, len(slides)-1)
        elif k == "q":
            print("bye!")
            break


def parse_turn(line):
    turn, player, action = line.split(": ")
    number = int(turn[5:])
    atype = action[:5]
    if atype == "THROW":
        aargs = (action[13], eval(action[18:]))
    else:
        aargs = tuple(map(eval, action.strip("SWINGLDE from").split(" to ")))
    return number, player, (atype, *aargs)


class Game:
    def __init__(self):
        ran = range(-4, +4+1)
        self.hexes = [(r, q) for r in ran for q in ran if r+q in ran]

        self.board = {x: collections.Counter() for x in self.hexes}
        self.throws = collections.Counter()
    
    def update(self, upper_action, lower_action):
        battles = []
        for player, action, case, iscase in (
            ("upper", upper_action, str.upper, str.isupper),
            ("lower", lower_action, str.lower, str.islower),
        ):
            atype, *aargs = action
            if atype == "THROW":
                s, x = aargs
                self.board[x][case(s)] += 1
                self.throws[player] += 1
                battles.append(x)
            else:
                x, y = aargs
                s = next(filter(iscase, +self.board[x]))
                self.board[x][s] -= 1
                self.board[y][s] += 1
                battles.append(y)
        # resolve hexes with new tokens:
        for x in battles:
            hex = self.board[x] # will mutate!
            types = {s.lower() for s in +hex}
            if 'r' in types:
                del hex['s']; del hex['S']
            if 'p' in types:
                del hex['r']; del hex['R']
            if 's' in types:
                del hex['p']; del hex['P']
    
    def display(self, message=""):
        board_template = """{00:}
        throws:        .-'-._.-'-._.-'-._.-'-._.-'-.
         upper        |{57:}|{58:}|{59:}|{60:}|{61:}|
         {62:}      .-'-._.-'-._.-'-._.-'-._.-'-._.-'-.
         lower     |{51:}|{52:}|{53:}|{54:}|{55:}|{56:}|
         {63:}   .-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-.
                |{44:}|{45:}|{46:}|{47:}|{48:}|{49:}|{50:}|
              .-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-.
             |{36:}|{37:}|{38:}|{39:}|{40:}|{41:}|{42:}|{43:}|
           .-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-.
          |{27:}|{28:}|{29:}|{30:}|{31:}|{32:}|{33:}|{34:}|{35:}|
          '-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
             |{19:}|{20:}|{21:}|{22:}|{23:}|{24:}|{25:}|{26:}|
             '-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
                |{12:}|{13:}|{14:}|{15:}|{16:}|{17:}|{18:}|
                '-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
                   |{06:}|{07:}|{08:}|{09:}|{10:}|{11:}|
                   '-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
                      |{01:}|{02:}|{03:}|{04:}|{05:}|
                      '-._.-'-._.-'-._.-'-._.-'-._.-'
        {64:}"""
        def _colour(a):
            if a.islower():
                return (fg.magenta + fx.bold)(a)
            elif a.isupper():
                return fx.bold(a)
            return a
        
        # construct the contents of the cells:
        cells = []
        overflows = []
        for x in self.hexes:
            symbols = list(self.board[x].elements())
            if len(symbols) == 0:
                cell = "     "
            elif len(symbols) == 1:
                cell = f" ({symbols[0]}) "
            elif len(symbols) == 2:
                cell = f"({symbols[0]}){symbols[1]})"
            else:  # len(symbols) >= 3
                cell = f"({symbols[0]}){len(symbols)})"
                overflows.append(f"{x}: {symbols}")
            cells.append("".join(map(_colour, cell)))
        return board_template.format(
            message,
            *cells,
            str(self.throws["upper"]).center(5),
            str(self.throws["lower"]).center(5),
            (
                "overflown hexes:\n+ " + "\n+ ".join(overflows)
                if overflows
                else ""
            ),
        )







if __name__ == "__main__":
    main()
