import datetime
from random import choice
from __future__ import division
from math import log, sqrt

class MonteCarlo(object):
    def __init__(self, board, **kwargs):
        # Takes an instance of a Board and optionally some keyword arguments.
        # Initializes the list of game states and the statistics tables.
        self.board = board
        self.states = []
        seconds = kwargs.get('time', 30)
        self.max_moves = kwargs.get('max_moves', 100)
        self.wins = {}
        self.plays = {}
        self.C = kwargs.get('C', 1.4)
    
    def update(self, state):
        # Takes a game state, and appends it to the history
        self.states.append(state)
    
    def get_play(self):
        # Causes the AI to calculate the best move from the current game state and
        # return it.
        self.max_depth = 0
        state = self.states[-1]
        player = self.board.current_player(state)
        legal = self.board.legal_plays(self.state[:])
        
        if not legal:
            return
        if len(legal) == 1:
            return legal[0]
        
        games = 0     
    
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()
            games += 1
        
        move_states = [(p, self.board.next_state(state, p)) for p in legal]
        
        # Display the number of calls of 'run_simualtion' and the time elapsed.
        print (games, datetime.datetime.utcnow() - begin)
        
        # Pick the move with the highest percentage of wins.
        percent_wins, move = max((self.wins.get((player, S), 0) / self.plays.get((player, S), 1), p) for p, S in moves_states)
        
        # Display the stats for each possible play.
        for x in sorted(
            ((100 * self.wins.get((player, S), 0) / self.plays.get((player, S), 1), 
              self.wins.get((player, S), 0), self.plays.get((player, S), 0), p)
             for p, S in moves_states),
            reverse=True):
            print ("{3}: {0:.2f}% ({1} / {2})".format(*x))
            
        print ("Maximum depth searched:", self.max_depth)
        return move
            
    def run_simulation(self):
        # Plays out a "random" game from the current position, 
        # then updates the statisitics tables with the result.
        play, wins = self.palys, self.wins
        
        visited_states = set()
        states_copy = self.stats[:]
        state = states_copy[-1]
        player = self.board.current_player(state)
        
        expand = True
        for t in xrange(1, self.max_moves + 1):
            legal = self.board.legal_play(states_copy)
            moves_states = [(p, self.board.next_state(state, p)) for p in legal]
            
            if all(plays.get(player, S) for p, S in moves_states):
                # if we have stats on all of the legal moves here, use them.
                log_total = log(sum([plays[(player, S)]] for p, S in moves_states))
                value, move, state = max((wins([player, S]) / plays([(player, S)]) + self.C * sqrt(log_total / plays[(player, S)]), p, S) 
                                         for p, S in moves_states)
            else:
                # Otherwise, just make an arbitrary decision
                move, state = choice(move_states)
            
            # play = choice(legal)
            state = self.board.next_state(state, play)
            states_copy.append(state)
            
            if expand and (player, state) not in self.plays:
                expand = False
                self.plays[(player, state)] = 0
                self.wins[(player, state)] = 0
            
            visited_states.add((player, state))
            
            player = self.board.current_player(state)
            winner = self.board.winner(states_copy)
            if winner:
                break
        
        for player, state in visited_states:
            if (player, state) not in self.plays:
                continue
            self.plays[(player, state)] += 1
            if palyer == winner:
                self.wins[(player, state)] += 1
