def eh_tabuleiro(tab):
    """
    recebe um tabuleiro e verifica se e valido ou nao
    """
    if type(tab) != tuple or len(tab) != 3:
        return False
    for i in tab:
        if type(i) != tuple or len(i) != 3:
            return False
        for x in i:
            if type(x) != int or x != 0 and x != 1 and x != -1:
                return False
    return True


def eh_posicao(p):
    """
    recebe uma posicao do tabuleiro e verifica se e valida
    """
    if type(p) != int or p > 9 or p < 1:
       return False
    return True


def obter_coluna(tab, c):
    """
    recebe um tabuleiro e o numero de uma coluna e devolve o tuplo que a representa
    """
    if type(c) != int or 1 > c or c > 3 or eh_tabuleiro(tab) is False:
        raise ValueError('obter_coluna: algum dos argumentos e inválido')
    res = ()
    for i in tab:
     res += (i[c-1],)
    return res


def obter_linha(tab, l):
    """
    recebe um tabuleiro e o numero de uma linha e devolve o tuplo que a representa
    """
    if type(l) != int or 1 > l or l > 3 or eh_tabuleiro(tab) is False:
        raise ValueError('obter_linha: algum dos argumentos e inválido')
    return tab[l-1]


def obter_diagonal(tab, d):
    """
    recebe um tabuleiro e o numero de uma diagonal e devolve o tuplo que a representa
    """
    if type(d) != int or (d != 1 and d != 2) or eh_tabuleiro(tab) is False:
        raise ValueError('obter_diagonal: algum dos argumentos e inválido')
    if d == 1:
        return (tab[0][0],) + (tab[1][1],) + (tab[2][2],)
    if d == 2:
        return (tab[2][0],) + (tab[1][1],) + (tab[0][2],)


def transformador(x):
    """
    recebe um elemento do tabuleiro como inteiro e transforma numa string representativa para o jogo
    """
    if x == 1:
        return 'X'
    elif x == 0:
        return ' '
    elif x == -1:
        return 'O'
    return False


def tabuleiro_str(tab):
    """
    recebe um tabuleiro e devolve uma string que o representa graficamente
    """
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    return ' {0} | {1} | {2} \n-----------\n {3} | {4} | {5} \n-----------\n {6} | {7} | {8} '.\
        format(*(transformador(x) for lines in tab for x in lines))


def eh_posicao_livre(tab, p):
    """
    recebe um tabuleiro e uma posicao e verifica se essa posicao e livre
    """
    if not (eh_tabuleiro(tab) and type(p) == int):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    if p > 9 or p < 1:
        return False
    res = ()
    for i in tab:
        for x in i:
            res += (x,)
    if res[p-1] != 0:
        return False
    return True


def obter_posicoes_livres(tab):
    """
    recebe um tabuleiro e devolve as suas posicoes livres
    """
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    res = ()
    for i in range(1, 10):
        if eh_posicao_livre(tab, i) is True:
            res += (i,)
    return res


def jogador_ganhador(tab):
    """
    recebe um tabuleiro e verifica se algum jogador ganha, se sim devolve o mesmo
    """
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')
    for i in range(1, 4):
        if obter_linha(tab, i) == (1, 1, 1):
           return 1
        if obter_coluna(tab, i) == (1, 1, 1):
           return 1
        if obter_linha(tab, i) == (-1, -1, -1):
           return -1
        if obter_coluna(tab, i) == (-1, -1, -1):
           return -1
    for x in range(1, 3):
        if obter_diagonal(tab, x) == (1, 1, 1):
            return 1
        if obter_diagonal(tab, x) == (-1, -1, -1):
            return -1
    return 0


def marcar_posicao(tab, x, p):
    """
    recebe um tabuleiro, um jogador e uma posicao e devolve um novo tabuleiro com a posicao alterada
    """
    if not (eh_tabuleiro(tab) and eh_posicao_livre(tab, p)) or (x != 1 and x != -1):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    newt = ()
    for i in tab:
        for n in i:
            newt += (n,)
    newt2 = newt[0:p-1] + (x,) + newt[p:]
    return (newt2[0:3]), (newt2[3:6]), (newt2[6:10])


def escolher_posicao_manual(tab):
    """
    recebe um tabuleiro e pede ao jogador para escolher uma posicao
    """
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_manual: algum dos argumentos e invalido')
    p = eval(input('Turno do jogador. Escolha uma posicao livre: '))
    if not eh_posicao_livre(tab, p):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    return p


def centro(tab):
    """
    recebe um tabuleiro e devolve a posicao central caso esteja livre
    """
    if eh_posicao_livre(tab, 5):
        return 5
    return False


def canto_vazio(tab):
    """
    recebe um tabuleiro e devolve um canto vazio caso haja
    """
    for p in (1, 3, 7, 9):
        if eh_posicao_livre(tab, p):
            return p
    return False


def lateral_vazio(tab):
    """
    recebe um tabuleiro e devolve uma lateral vazia caso haja
    """
    for p in (2, 4, 6, 8):
        if eh_posicao_livre(tab, p):
            return p
    return False


def vitoria(tab, x):
    """
    recebe um tabuleiro e as pecas do jogador e devolve uma posicao que leve a vitoria caso haja
    """
    for i in range(1, 4):
        if obter_coluna(tab, i) == (x, x, 0):
            return i + 6
        if obter_coluna(tab, i) == (x, 0, x):
            return i + 3
        if obter_coluna(tab, i) == (0, x, x):
            return i
        if obter_linha(tab, i) == (x, x, 0):
            return i * 3
        if obter_linha(tab, i) == (x, 0, x):
            return (i * 3) - 1
        if obter_linha(tab, i) == (0, x, x):
            return (i * 3) - 2
    for i in range(1, 3):
        if obter_diagonal(tab, i) == (x, x, 0):
            return (i + 8 // i) // i
        if obter_diagonal(tab, i) == (x, 0, x):
            return 5
        if obter_diagonal(tab, i) == (0, x, x):
            return (i * i * 2) - 1
    return False


def bloqueio(tab, x):
    """
    recebe um tabuleiro e as pecas do jogador e devolve uma posicao que bloqueie a vitoria do adversario caso haja
    """
    return vitoria(tab, -x)


def canto_oposto(tab, x):
    """
    recebe um tabuleiro e as pecas do jogador e devolve a posicao do canto oposto ao canto onde esta o adversario
    """
    res = ()
    for e in tab:
        for i in e:
            res += (i,)
    for p in (1, 3, 7, 9):
        if eh_posicao_livre(tab, p) and res[(9 - p)] == -x:
            return p
    return False


def bifurcacao(tab, x):
    """
    recebe um tabuleiro e as pecas do jogador e devolve as posicoes que criam bifurcacoes
    """
    for p in range(1, 4):
        if obter_linha(tab, p) == ((x, x, 0) or (x, 0, x) or (0, x, x)):
            return 5
        if obter_coluna(tab, p) == ((x, x, 0) or (x, 0, x) or (0, x, x)):
            return 5
        for i in range(2, 4):
            if x in obter_linha(tab, p) and x in obter_coluna(tab, i):
                if eh_posicao_livre(tab, i * p):
                    return i * p
    return False


def bloqueio_bifurcacao(tab, x):
    """
    recebe um tabuleiro e as pecas do jogador e devolve as posicoes de bloqueio a possiveis bifurcacoes do oponente
    """
    return bifurcacao(tab, -x)


def estrategia(nivel):
    """
    recebe uma estrategia e valida
    """
    if nivel != 'basico' and nivel != 'normal' and nivel != 'perfeito':
        return False
    return True


def escolher_posicao_auto(tab, x, nivel):
    """
    recebe um tabuleiro, as pecas do jogador e uma estrategia e devolve a posicao adequada
    """
    if not (x == 1 or x == -1) or not eh_tabuleiro(tab) or not estrategia(nivel):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    if nivel == 'basico':
        if centro(tab):
            return centro(tab)
        if canto_vazio(tab):
            return canto_vazio(tab)
        if lateral_vazio(tab):
            return lateral_vazio(tab)
    if nivel == 'normal':
        if vitoria(tab, x):
            return vitoria(tab, x)
        if bloqueio(tab, x):
            return bloqueio(tab, x)
        if centro(tab):
            return centro(tab)
        if canto_oposto(tab, x):
            return canto_oposto(tab, x)
        if canto_vazio(tab):
            return canto_vazio(tab)
        if lateral_vazio(tab):
            return lateral_vazio(tab)
    if nivel == 'perfeito':
        if vitoria(tab, x):
            return vitoria(tab, x)
        if bloqueio(tab, x):
            return bloqueio(tab, x)
        if bifurcacao(tab, x):
            return bifurcacao(tab, x)
        if bloqueio_bifurcacao(tab, x):
            return bloqueio_bifurcacao(tab, x)
        if centro(tab):
            return centro(tab)
        if canto_oposto(tab, x):
            return canto_oposto(tab, x)
        if canto_vazio(tab):
            return canto_vazio(tab)
        if lateral_vazio(tab):
            return lateral_vazio(tab)
    return False


def jogo_do_galo(j, nivel):
    """
    recebe as pecas do jogador e a estrategia e devolve o jogo completo
    """
    if not estrategia(nivel) or not (j == 'X' or j == 'O'):
        raise ValueError('jogo do galo: algum dos argumentos e invalido')
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com '" + j + "'.")
    while len(obter_posicoes_livres(tab)) > 0:
        if j == 'X':
            tab = marcar_posicao(tab, 1, escolher_posicao_manual(tab))
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == 1:
                return 'VITORIA'
            if obter_posicoes_livres(tab) == () and jogador_ganhador(tab) == 0:
                return 'EMPATE'
            print('Turno do computador (' + nivel + '):')
            tab = marcar_posicao(tab, -1, escolher_posicao_auto(tab, -1, nivel))
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == -1:
                return 'DERROTA'
        if j == 'O':
            if jogador_ganhador(tab) == -1:
                return 'VITORIA'
            print('Turno do computador (' + nivel + '):')
            tab = marcar_posicao(tab, 1, escolher_posicao_auto(tab, 1, nivel))
            print(tabuleiro_str(tab))
            if obter_posicoes_livres(tab) == () and jogador_ganhador(tab) == 0:
                return 'EMPATE'
            if jogador_ganhador(tab) == 1:
                return 'DERROTA'
            tab = marcar_posicao(tab, -1, escolher_posicao_manual(tab))
            print(tabuleiro_str(tab))
    return 'EMPATE'
