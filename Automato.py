"""Automato Module holds the Automato class"""


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
            transitions of the automaton: eg {(1, "a"): 1}
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

    #eh um automato deterministico?
    def __deterministic(self):
        """determin if that automaton is deterministic
        Returns: boolean
            True if there is more than one possible state for at least one
        transition
        """
        for transition in self.__transitions:
            next_states = self.__transitions[transition]
            if len(next_states) > 1:
                # mais de um possivel proximo estado para uma mesma transicao
                return True
        return False

    #simular automato finito
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

    #simular automato derteministico
    def __dfa_simulate(self, string, current_state):
        """simulate deterministic automaton
        Args:
            string: string to be recognized
        Returns: boolean
            True if automaton recognizes the string
        """
        if string == "":
            # se string estiver vazia
            return (current_state in self.__accepting_states)
            # True se esta em estado aceitador
        else:
            character = string[0]
            # pega primeiro caracter da string de entrada
            if (current_state, character) in self.__transitions:
                # ve se ha transicao naquele estado com este caracter
                next_state = self.__transitions[(current_state, character)]
                remaining_string = string[1:]
                return self.__dfa_simulate(remaining_string, next_state)
            else:
                return False
                # nao existe transicao nesse estado com este caracter

    #simulateular automato nao deterministico
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
                for next_state in next_states:
                    # simulateula para cada um dos estados
                    result = self.__ndfa_simulate(remaining_string, next_state)
                    if result:
                        return True
                        # um dos ramos aceitou,
                        # nao precisa continuar simulateulacao
                return False
                # nenhum ramo aceitou
            else:
                return False
                # nao existe transicao nesse estado com este caracter

    #def determinize(self):
     #   if self.__is_deterministic:
      #      return self
       # ....
