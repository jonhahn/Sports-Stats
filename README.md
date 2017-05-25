# Sports-Stats
This repository has a few scripts related to predicting sports.

March Madness
    The pool I am a part of has the follorules:
        1. Pick 8 teams
        2. No 2 teams may have the same seed number
        3. The total of your teams seed numbers may not exceed 62
        4. Whoever has the most wins at the end of the tournament wins. Wins are not weighted.

    The scripts use the odds of winning from the FiveThirtyEight blog to come up with the 8 teams with the highest expected number of wins.


Cribbage
    I am in a two person tournament with the following rules.
        1. Win 3 Games in a row to earn a Set 
        2. Win 3 Sets in a row to earn a Match (losing Games is okay, but opponent may not win a Set between your 3 Sets)
        3. Win 3 Matches in a row to win the tournament (losing Games and Sets is okay, but opponent may not win a Match between yours)

        The script determines, given the current scoreboard (Games, Sets, Matches won in a row by each player), what the odds are that player 1 wins outright, and the expected number of games left (which = 367 at the start)