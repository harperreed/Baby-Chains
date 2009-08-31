'''

Tweaked from:

Filename: markov_chain.py
Copyright: Yongqian Li
License: This code is released under GPLv3
'''
class MarkovChain:
    def __init__(self):
        self.transition_table = {}
        self.state_count = {}
    
    def add_str(self, s):
        s = ' ' + s + ' '
        def add_transitions(l):
            for i in range(len(s)-l):
                self.add_transition(s[i:i+l], s[i+l])
        add_transitions(0)
        add_transitions(1)
        add_transitions(2)
        add_transitions(3)
        add_transitions(4)

    def add_transition(self, state, next):
        if state not in self.transition_table:
            self.transition_table[state] = {}
            self.state_count[state] = 0
        if next not in self.transition_table[state]:
            self.transition_table[state][next] = 0
        self.state_count[state] += 1
        self.transition_table[state][next] += 1
    
    def get_prob(self, state, next):
        if state in self.transition_table:
            if next in self.transition_table[state]:
                return self.transition_table[state][next] / float(self.state_count[state])
        return self.get_prob(state[1:], next) #lookup in lower order #0.0
    
    def get_probs(self, state):
        #return dict((k, v / float(self.state_count[state])) for k, v in self.transition_table[state].iteritems())
        #return dict((k, self.get_prob(state, k)) for k in self.transition_table[state])
        return dict((next, self.get_prob(state, next)) for next in 'abcdefghijklmnopqrstuvwxyz ')                

    def generate(self, s, count=2, num_results=50):
        states = [(' ' + s, 1.0)]
        for c in range(count):
            next_states = []
            for state, prob in states:
                for k, v in self.get_probs(state[-3:]).iteritems():
                    if k != ' ':
                        next_states.append((state + k, prob * v))
            next_states.sort(key=lambda x: x[1], reverse=True)
            states = next_states[:num_results]
        states = [(k[1:], v * self.get_prob(k, ' ')) for k, v in states]
        states.sort(key=lambda x: x[1], reverse=True)
        assert states == self.project2(s, count)
        return states

    def generate(self, s, count=2, num_results=50):
        states = [(' ' + s, 1.0)]
        for c in range(count):
            next_states = []
            for state, prob in states:
                for k, v in self.get_probs(state).iteritems():
                    if k != ' ':
                        next_states.append((state + k, prob * v))
            next_states.sort(key=lambda x: x[1], reverse=True)
            states = next_states[:num_results]
        states = [(k[1:], v * self.get_prob(k, ' ')) for k, v in states]
        states.sort(key=lambda x: x[1], reverse=True)
        return states
    
markov_chain = MarkovChain()
#markov_chain_r = MarkovChain()


f = open('names.lst')
for line in f:
    s = line.strip()
    markov_chain.add_str(s)
    #markov_chain_r.add_str(''.join(reversed(s)))


def main():
    #Usage: python markov_chain.py <initial> <length>
    import sys
    initial = sys.argv[1]
    if len(sys.argv) == 3:
        length = int(sys.argv[2])
    else:
        length = 3
    #s = sorted(markov_chain.generate(initial).iteritems(), key=lambda x: x[1], reverse=True)
    s = markov_chain.generate(initial, length)
    for d, p in s:
        print d

if __name__ == '__main__':
    main()
