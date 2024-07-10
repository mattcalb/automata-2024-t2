"""Implementação de autômatos finitos."""


def load_automata(filename):
    with open(filename, "rt") as arquivo:
        content = arquivo.readlines()
        content = [line.split() for line in content]
        cont = 0
        for state in content[2]:
            if(state in content[1]):
                cont = cont + 1
        if(cont < len(content[2])):
            raise Exception('Estados finais não estão presentes no conjunto de estados')
        if(len(content[1]) == 1 and content[3] != content[1]):
            raise Exception('Estado inicial não está presente no conjunto de estados')

        elif(len(content[1]) > 1):
            cont = 0
            for state in content[1]:
                if(content[3][0] == state):
                    cont = cont + 1
                if(cont < 1):
                    raise Exception('Estado inicial não está presente no conjunto de estados')
        return content


def process(automata, words):
    result = {}
    for x in words:
        currentState = ''.join(automata[3])
        splitWord = [i for i in x]
        for y in splitWord:
            if(y not in automata[0]):
                result[x] = 'INVALIDA'
        cont = 0
        if(x not in result):
            while(cont < len(splitWord)):
                for states in automata[4:]:
                    for state in states:
                        if(currentState == state and cont < len(splitWord)):
                            if(splitWord[cont] == states[1]):
                                currentState = states[2]
                                cont = cont + 1
                        break
            if(currentState in automata[2]):
                result[x] = 'ACEITA'
            else:
                result[x] = 'REJEITA'
    return result

'''
def convert_to_dfa(automata):
    inicial = automata[3]


    novasTransicoes = []
    checados = []
    novosEstados = []
    paraChecar = [set(inicial)]
    allStates = []
    finalStates = []

    while len(paraChecar) > 0:
        atual = paraChecar.pop(0)
        checados.append(atual)

        podeContinuar = True	

        letras = {letra: [] for letra in automata[0]}

        for connection in automata[4:]:
            if connection[0] in atual:
                letra = connection[1]

                if letra == '&' and connection[2] not in atual:
                    podeContinuar = False
                    
                    novo = atual.union({connection[2]})

                    if novo not in checados:
                        paraChecar.insert(0, novo)
                    
                    if atual == set(inicial):
                        inicial = set(list(novo)[:])
                
                elif letra != '&':
                    letras[letra].append(connection)
        
        if podeContinuar == False:
            continue	
        
        if atual not in novosEstados:
            novosEstados.append(atual)

        for letra in letras:
            if len(letras[letra]) > 1:
                novo = set()
                for array in letras[letra]:
                    novo.add(array[2])

                novo = novo.union(atual)

                if novo not in checados:
                    paraChecar.insert(0, novo)
            
            elif len(letras[letra]) > 0:
                if letras[letra][0][2] not in checados:
                    paraChecar.insert(0, {letras[letra][0][2]})

    initialFinalStates = set(automata[2])
    for i, state in enumerate(novosEstados):
        if len(initialFinalStates.intersection(state)) > 0:
            novosEstados[i].add('f')
        
        else:
            novosEstados[i].add('n')

    for estado in novosEstados:
        isFinal = 'f' in estado
        new = ''.join(sorted(list(estado)))[1:]

        allStates.append(new)

        if isFinal:
            finalStates.append(new)


    return (automata[0], allStates, finalStates,''.join(sorted(list(inicial))), novasTransicoes)'''