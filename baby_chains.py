import sys,os
from markov import Markov

if __name__ == "__main__":
    #Usage: python baby_chains.py <length>
    if len(sys.argv) == 2:
        number_names = int(sys.argv[1])
    else:
        number_names = 30

    training_text = 'names.lst'
    markovchain = Markov()
    f = open(training_text, 'r')
    print "Loading "+training_text+" into brain."
    markovchain.load_brain(f)
    print 'Brain Reloaded'
    f.close()
    names = markovchain.generate_simple_sentence(number_names)
    print "Outputting " + str(number_names) + " generated names"
    print "\n".join(names)

