"""Automato Module holds the Automato class"""

__authors__ = 'Diego Izidoro e Peterson C. Oliveira'


class Automato:
    """Automato class:

    No public attributes
    Public methods:
        __init__(transitions, initial_state, accepting_states)
        is_deterministic()
        fa_simulate(string)
    """

    def __init__(self, transitions, initial_state, accepting_states):
        """instanciates a automaton.
        Args:
            transitions of the automaton: eg. dfa -- {(1, "a"): 1} or
                                             ndfa -- {(1, "b"): [1,2]}
            initial_state: state automaton starts recognizement
            accepting_states: list of automaton accepting states
        """
        assert transitions.__class__ == dict
        assert accepting_states.__class__ == list
        self.__transitions = transitions
        self.__initial_state = initial_state
        self.__accepting_states = set(accepting_states)
        self.__is_deterministic = self.__deterministic()

    def is_deterministic(self):
        """answers if automaton is deterministic
        Returns: boolean
            True if automaton is determistic
            False otherwise
        """
        return self.__is_deterministic

    def __deterministic(self):
        """determin if the automaton is deterministic
        Returns: boolean
            True if there isn't more than one possible state for at least one
        transition
        """
        for transition in self.__transitions:
            next_states = self.__transitions[transition]
            if next_states.__class__ == list:  # mais de um possivel proximo estado para uma mesma transicao
                return False
        return True

    def is_empty(self):
        """determin if the automaton recognizes no string
        Returns: boolean or string
            True if does not recognizes any string, not even epsilon
            An example string it accepts
        """
        return __is_empty(self.__initial_state)

    def __is_empty(self, current_state, visited=[]):
        """determin if the automaton recognizes no string
        Args:
            current_state: state we are currently visiting
            visited: list of visited
        Returns: boolean or string
            True if recognizes no strings, not even epsilon
            An example string it accepts
        """
        if current_state in visited:
            return True
        visited.append(current_state)
        if current in accepting:
            return ""
        for (state, character), next_states in self.__transitions.items():
            if state == current_state:
                for next_state in next_states:
                    result = is_empty(next_state, visited)
                    if result is not    True:
                        return character + result
        return True

    def fa_simulate(self, input_string):
        """simulates the finite automato recongnizement
        Args:
            input_string: string to be recognized or ...not!
        Returns: boolean
            True if automaton recognizes the input_string
        """
        assert input_string.__class__ == str
        if self.__is_deterministic:
            return self.__dfa_simulate(input_string, self.__initial_state)
        else:
            return self.__ndfa_simulate(input_string, self.__initial_state)

    def __dfa_simulate(self, string, current_state):
        """simulate deterministic automaton
        Args:
            string: string to be recognized
        Returns: boolean
            True if automaton recognizes the string
        """
        if string == "":
            return (current_state in self.__accepting_states)  # True se esta em estado aceitador
        else:
            character = string[0]
            if (current_state, character) in self.__transitions:
                next_state = self.__transitions[(current_state, character)]
                remaining_string = string[1:]
                return self.__dfa_simulate(remaining_string, next_state)
            else:
                return False

    def __ndfa_simulate(self, string, current_state):
        """simulate non-deterministic automaton
        Args:
            string: string to be recognized
            current_state: holds automaton's current state
        Returns: boolean
            True if automaton recognizes the string
        """
        if string == "":
            return (current_state in self.__accepting_states)
        else:
            character = string[0]
            if (current_state, character) in self.__transitions:
                next_states = self.__transitions[(current_state, character)]
                remaining_string = string[1:]
                for next_state in next_states:  # Simula para cada um dos possiveis estados
                    result = self.__ndfa_simulate(remaining_string, next_state)
                    if result:
                        return True  # Um dos ramos aceitou
                return False
            else:
                return False
