'''
Figure out the probability of Logan winning.
'''

import numpy as np

class GameState(object):

    def __init__(self, index, gw=0, gl=0, sw=0, sl=0, mw=0, ml=0):
        self.game_w = gw
        self.game_l = gl
        self.set_w = sw
        self.set_l = sl
        self.match_w = mw
        self.match_l = ml

        self.Logan_goes_first = 0   #unused for now

        self.index = index

        self.index_if_loss = -1
        self.index_if_win = -1

    def is_it_me(self, state):
        if state == self.my_state():
            return 1
        else:
            return 0

    def my_state(self):
        return [(self.game_w, self.game_l), (self.set_w, self.set_l), (self.match_w, self.match_l)]

    def state_if_loss(self):
        game_w = 0

        game_l = self.game_l + 1
        if game_l == 3:
            game_l = 0
            set_w = 0
            set_l = self.set_l + 1
            if set_l == 3:
                set_l = 0
                match_w = 0
                match_l = self.match_l + 1
            else:
                match_l = self.match_l
                match_w = self.match_w
        else:
            set_w = self.set_w
            set_l = self.set_l
            match_l = self.match_l
            match_w = self.match_w

        return [(game_w, game_l), (set_w, set_l), (match_w, match_l)]

    def state_if_win(self):
        game_l = 0

        game_w = self.game_w + 1
        if game_w == 3:
            game_w = 0
            set_l = 0
            set_w = self.set_w + 1
            if set_w == 3:
                set_w = 0
                match_l = 0
                match_w = self.match_w + 1
            else:
                match_w = self.match_w
                match_l = self.match_l
        else:
            set_w = self.set_w
            set_l = self.set_l
            match_l = self.match_l
            match_w = self.match_w

        return [(game_w, game_l), (set_w, set_l), (match_w, match_l)]


class System(object):

    def __init__(self):

        state_possibilities = [(0,0), (1,0), (0,2), (0,1), (2,0)]

        index = 0
        game_states = []
        for games in state_possibilities:
            for sets in state_possibilities:
                for matches in state_possibilities:

                    gw = games[0]
                    gl = games[1]
                    sw = sets[0]
                    sl = sets[1]
                    mw = matches[0]
                    ml = matches[1]
                    game_states.append(GameState(index, gw, gl, sw, sl, mw, ml))
                    index += 1

        self.game_states = game_states

        #for index in xrange(125):
        #    print game_states[index].my_state(), index

        self.link_states()
        self.set_up_odds_matrix()
        self.set_up_expected_games_left_matrix()
        
        '''
        for state in game_states:
            if state.is_it_me(state_if_win):
                print 'State If Win ', state.my_state(), state.index
                win_index = state.index
                gs.index_if_win = win_index
        for state in game_states:
            if state.is_it_me(state_if_loss):
                print 'State If Loss ', state.my_state(), state.index
                loss_index = state.index
                gs.index_if_loss = loss_index
        print
        

        self.A = np.zeros((125, 125))
        #print self.A
        for index in xrange(125):
            self.A[index, index] = -1
            w = game_states[index].index_if_win
            l = game_states[index].index_if_loss
            if w >= 0:
                self.A[index, w] = .5
            if l >= 0:
                self.A[index, l] = .5
        #print self.A[0,:]

        self.b = np.zeros((1,125))
        self.b[0,124] = -.5 
        print self.b

        self.x = np.linalg.solve(self.A, (self.b).T)
        print self.x

        #print np.dot(self.A, self.x)
        '''

    def link_states(self):
        for gs in self.game_states:
            state_if_win = gs.state_if_win()
            state_if_loss = gs.state_if_loss()
            #print gs.index, gs.my_state()
            gs.index_if_win = self.find_game_state_index(state_if_win)
            gs.index_if_loss = self.find_game_state_index(state_if_loss)

    def set_up_odds_matrix(self):
        self.A = np.zeros((125, 125))
        #print self.A
        for index in xrange(125):
            self.A[index, index] = -1
            w = self.game_states[index].index_if_win
            l = self.game_states[index].index_if_loss
            if w >= 0:
                self.A[index, w] = .5
            if l >= 0:
                self.A[index, l] = .5
        #print self.A[0,:]

        self.b = np.zeros((1,125))
        self.b[0,124] = -.5 
        #print self.b

        self.odds = np.linalg.solve(self.A, (self.b).T)
        #print self.x

        return

    def set_up_expected_games_left_matrix(self):
        self.AA = np.zeros((125, 125))
        self.bb = np.zeros((1,125))

        for index in xrange(125):
            self.AA[index, index] = -1
            w = self.game_states[index].index_if_win
            l = self.game_states[index].index_if_loss
            if w >= 0:
                self.AA[index, w] = .5
            if l >= 0:
                self.AA[index, l] = .5

            self.bb[0,index] = -1
        print self.AA[2]

        self.expected_games_left= np.linalg.solve(self.AA, (self.bb).T)
        print self.expected_games_left

        return

    def find_game_state_index(self, state):
        for gs in self.game_states:
            if state == gs.my_state():
                return gs.index
        return -1

            #print gs.my_state(), game_states[gs.index_if_win].my_state(), game_states[gs.index_if_loss].my_state()
if __name__ == "__main__":
    system = System()
    current_state = [(0,1),(2,0),(2,0)]
    current_state_index = system.find_game_state_index(current_state)
    current_odds = system.odds[current_state_index]
    current_games_left = system.expected_games_left[current_state_index]
    print current_state, current_odds, current_games_left


