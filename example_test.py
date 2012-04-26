"""Test example for simulating an Automato"""
from Automato import Automato

__authors__ = 'Diego Izidoro e Peterson C. Oliveira'


def main():
    """main"""
    transitions = {(0, "a"): [1],  # (estado, "caracter") : [lista de estados]
                    (1, "b"): [1]}

    initial_state = 0
    accepting_states = [1]
    automato = Automato(transitions, initial_state, accepting_states)

    print "Automaton"
    print "========="
    print "Transitions: " + str(transitions)
    print "Initial state: " + str(initial_state)
    print "Accepting states:" + str(accepting_states)
    print
    print "Tests"
    print "====="
    print "Automaton accepts 'a': " + str(automato.fa_simulate("a"))
    print "Automaton accepts 'ab': " + str(automato.fa_simulate("ab"))
    print "Automaton accepts 'aba': " + str(automato.fa_simulate("aba"))
    print "Automaton accepts 'abbbb': " + str(automato.fa_simulate("aba"))
    print

    string = raw_input("Your turn, insert a string :")
    result = automato.fa_simulate(string)

    if(result):
        print "Your string was accepted by the automaton!"
    else:
        print "Your string was NOT accepted by the automaton!"


if __name__ == '__main__':
    main()
