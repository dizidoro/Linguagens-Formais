class Automato:
    
    def __init__(self, transitions, initial_state, accepting_states):
        assert transistions.__class__ == {}.__class__
        assert initial_state.__class == (1).__class__
        assert accepting_states.__class__ == [].__class__   
        self.__transitions = transitions
        self.__initial_state = initial_state
        self.__accepting_states = set(accepting_states)
        self.__is_dfa = self.is_dfa()
        
        
    def is_dfa(self):
        for transition in self.__transitions:
            next_states = self.__transitions[transition]
            if len(next_states) > 1: #mais de um possivel proximo estado para uma mesma transicao
                return True
        return False
        
    #simular automato finito
    def fa_sim(self, input_string):
        assert input_string.__class__ == "".__class__
        if self.__is_dfa:
            return self.__dfa_sim(input_string, self.__initial_state)
        else:
            return self.__ndfa_sim(input_string, self.__initial_state)
            
            
    #simular automato derteministico
    def __dfa_sim(self, string, current_state):
        if string == "": #se string estiver vazia
            return (current_state in self.__accepting_states) #True se esta em estado aceitador
        else:
            character = string[0] #pega primeiro caracter da string de entrada
            if (current_state, character) in self.__transitions: #ve se ha transicao naquele estado com este caracter
                next_state = self.__transitions[(current_state, character)]
                remaining_string = string[1:]
                return self.__dfa_sim(remaining_string, next_state)
            else:
                return False #nao existe transicao nesse estado com este caracter
            
                
    #simular automato nao deterministico
    def __ndfa_sim(self, string, current_state):
        if string == "":
            return (current_state in self.__accepting_states)
        else:
            character = string[0]
            if (current_state, character) in self.__transitions:
                next_states = self.__transitions[(current_state, character)]
                remaining_string = string[1:]
                for next_state in next_states: #simula para cada um dos estados
                    result = self.__ndfa_sim(remaining_string, next_state)
                    if result:
                        return True #um dos ramos aceitou, nao precisa continuar simulacao
                return False #nenhum ramo aceitou
            else:
                return False #nao existe transicao nesse estado com este caracter

    
    #def determinize(self):
     #   if self.__is_dfa:
      #      return self        
       # .... 
    
    