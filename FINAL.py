#projeto 1 Fprog 21/22 LEIC
#ist1102507
#Sara Pinheiro
#sara.pinheiro@tecnico.ulisboa.pt

#1.1 corrigir_palavra
def corrigir_palavra(string):
    '''Função que recebe uma string que corresponde a uma palavra modificada 
    por um surto de letras e retorna essa palavra corrigida.
    -Input de uma string que irá ser essa palavra modificada-string(nome da 
    variável)
    -Retorna essa mesma string corrigida - string.
    corrigir_palavra: cad. carateres--->cad. carateres
    '''
    cont=0
    new_string=''
    l_string=len(string)
    while cont!=-1:
        
        for i in range(0,l_string-1):
            if abs(ord(string[i])-ord(string[i+1]))==32:
                string=string[:i]+string[i+2:]
                l_string=len(string)
                break
            
        if new_string==string:
            cont=-1
        new_string=string
        
    return string

#1.2 eh_anagrama 
def eh_anagrama(str1,str2):
    '''Função que retorna se duas palavras são anagramas ou não.
    -Input de duas strings que serão as duas palavras a avaliar -str1,str2
    -retorna um booleano (True se as duas palavras forem anagramas, False 
    se não forem)
    eh_anagrama: cad. carateres x cad. carateres--->booleano
    '''
    if len(str1)!=len(str2):
        return len(str1)==len(str2)
    
    str1,str2=list(str1),list(str2)
    for i in range(0,len(str1)):
        if ord(str1[i])<97:   
            str1[i]=chr(ord(str1[i])+32)
        if ord(str2[i])<97:
            str2[i]=chr(ord(str2[i])+32)
         
    str1,str2=sorted(str1),sorted(str2)
    
    return str1==str2

#1.3 corrigir_doc
def corrigir_doc(string):
    '''Função que, ao se fazer input de uma entrada com erros, devolve
    essa entrada corrigida e com os anagramas que são palavras 
    diferentes retirados.
    -Input de uma string -string- que corresponde a entrada com erros
    -Devolve uma nova string -string_f que corresponde à entrada corrigida
    corrigir_doc: cad. carateres --->cad. carateres
    '''
    cont=0
    if type(string)!=str or string=='':
        raise ValueError ('corrigir_doc: argumento invalido')
    len_str=len(string)
    for i in  range (0,len_str):
        if i==0 and string[i]==' ':
            raise ValueError ('corrigir_doc: argumento invalido')
        if i!=0:
            if ord(string[i])==32 and ord(string[i])==ord(string[i-1]):
                raise ValueError('corrigir_doc: argumento invalido')
            if ord(string[len_str-1])==32:
                raise ValueError('corrigir_doc: argumento invalido')
            if ord(string[i])==32:
                cont+=1  
            if ord(string[i])<65 and ord(string[i])!=32:
                raise ValueError('corrigir_doc: argumento invalido')     
            if 97>ord(string[i])>90 or ord(string[i])>122:
                raise ValueError('corrigir_doc: argumento invalido')
    #ciclos para validar o argumento; se esta na forma correta 1 unico espaco
    #entre palavras e se o tipo eh string  
    
    
    string=string.split()
    
    #visto que corrigir_palavra só pode corrigir uma palavra de cada vez:
    for palavra in range(0,len(string)):
        string[palavra]=corrigir_palavra(string[palavra])
        
    cont=0
    len_l=len(string)
    string_f=''
    i=0
    #i e y equivalem a índices 
    while i in range(0,len(string)):
        for y in range(0,len_l):
            if eh_anagrama(string[i],string[y-cont])==True and \
            string[i].lower()!=string[y-cont].lower():
                if i<y:
                    del(string[y-cont])
                    cont+=1
        i+=1
    for i in range(0,len(string)):
        if i!=0:
            string_f+=' '+ string[i]
        else:
            string_f+=string[i]
    return string_f

#2.1 obter_posicao
def obter_posicao (car,p_atual):
    '''Função que recebe uma posição atual e uma direção de movimento. 
     Devolve a posição final após movimento.
     
    -Input deve ser feito de uma string (correspondente a direção do 
    movimento- car) e um número inteiro positivo entre 1 e 9 (ambos incluidos), 
    correspondente a posição original -p_atual.
    -Será devolvido um outro inteiro entre 1 e 9 (incluidos) correspondente
    a nova posição após movimentos- p_nova.
    obter_posicao: cad. carateres x inteiro--->inteiro
    '''
    if car == 'C':
        p_nova= p_atual-3
        if p_nova < 1:
            p_nova=p_atual
    elif car =='B':
        p_nova=p_atual+3
        if p_nova>9 :
            p_nova=p_atual
    elif car=='D':
        p_nova=p_atual+1
        if p_nova==4 or p_nova==7 or p_nova>9:
            p_nova=p_atual
     
    elif car =='E':
        p_nova=p_atual-1
        if p_nova==3 or p_nova==6 or p_nova<1:
            p_nova=p_atual        
    return p_nova

#2.2 obter_digito
def obter_digito (car,pos):
    '''Função que devolve o dígito após movimento.
    -Input de uma string que corresponde uma ou mais sequências de movimentos -
    - car, e de um número inteiro positivo (entre 1 e 9, ambos incluídos) que 
    corresponde a posição inicial - pos.
    -Devolve outro inteiro positivo entre 1 e 9, incluídos, sendo o dígito
    após movimento- pos (depois de alterado).
    obter_digito: cad. carateres x inteiro--->inteiro
    '''
    ins= tuple(car)
    for i in ins:
        p_nova=obter_posicao(i,pos)
        pos=p_nova
    return pos

#2.3 obter_pin
def obter_pin(sequencias):
    '''Função que devolve o pin correspondente ao movimento de dígitos por 
    ordem de uma sequência.
    -Input de um tuple que tem 4 a 10 sequências do tipo string:(C,D,E,B) 
    -sequencias.
    -Devolve um outro tuple -tuplefinal- que será o pin.
    -Função tem duas partes: parte da validação de argumento e a parte de 
    seguir as instruções indicadas.
    obter_pin: tuplo--->tuplo
    '''
    if type(sequencias)!=tuple: 
        raise ValueError ('obter_pin: argumento invalido') 
    l_seq=len(sequencias)
    if sequencias==() or l_seq<4 or l_seq>10:
        raise ValueError ('obter_pin: argumento invalido')
    #verificacao do tipo e verificacao do nr de sequencias de movimentos
    
    #verificacao dos elementos, se sao instrucoes validas
    for i in range(0,l_seq):
        if i=='' or len(sequencias[i])<1:
            raise ValueError('obter_pin: argumento invalido')
        for y in sequencias[i]:
            if y != 'B' and y!='C' and y!='D' and y!='E':
                raise ValueError ('obter_pin: argumento invalido')
   
    tuplefinal=()
    posicao = 5
    for i in sequencias:
        tuple_i = tuple(i)
        tuplefinal+=(obter_digito(i, posicao),)
        posicao=obter_digito(i, posicao)
    
   
    return  tuplefinal

#3.1 e 4.1 eh_entrada 
def eh_entrada(tup):
    '''Função que devolve o booleano sobre se o argumento é uma entrada da BDB.
    -Input de qualquer tipo, universal -tup.
    -Devolve True ou False de acordo com as especificações de uma entrada.
    eh_entrada: universal--->booleano
    '''
    if type (tup)!= tuple or len(tup)!=3 or type(tup[2])!=tuple or \
       type(tup[0])!= str or type(tup[1])!=str:
        return False 
    
    cifra_tup,s_controlo,s_seguranca=tuple(tup[0]),tuple(tup[1]),tup[2]
    
    for i in cifra_tup:
        if (97>ord (i) or ord(i)>122) and ord(i)!=45: 
            return False
        if i==cifra_tup[0] or i== cifra_tup[len(cifra_tup)-1]:
            if ord(i)==45:
                return False
    for i in range(1,len(cifra_tup)-1):
        if ord(cifra_tup[i])==45 and ord(cifra_tup[i+1])==45:
            return False
    len_controlo=len(s_controlo)
    
    for i in range(0,len_controlo):
        if len_controlo!=7 or (i==0 and ord(s_controlo[i])!=91) or \
           (i==6 and ord(s_controlo[i])!=93):
            return False
        if 0<i and i<6:
            if ord (s_controlo[i])<97 or ord (s_controlo[i])>122:
                return False

    for i in s_seguranca:
        if type(i)!=int or len(s_seguranca)<2 or i<0:
            return False
    
    return True   
    
 #3.2 validar_cifra
 
def validar_cifra(cif,s_c):
    '''Função que devolve True se uma sequência de controlo está de acordo com
    a cifra. Devolve False se não está.
    -Input de duas strings, a cifra- cif- e a sequência de controlo - s_c
    -Devolve um valor booleano, True ou False
    validar_cifra: cad. carateres x cad. carateres ---> booleano
    '''
    len_cif=len(cif)
    cont={}
    for i in cif:
        if i in cont and ord(i)!=45:
            cont[i]+=1
        if i not in cont and ord(i)!=45:
            cont[i]=1 
    # parte de contar as ocorrências de cada letra na cifra
    
    lista_vlr,lista_key,cont_1=[],[],0
    len_cont,lista_final=len(cont),[]
    while len(lista_final)!=len_cont:
        for i in cont:
            lista_vlr+=[cont[i]]
        m_valor=max(lista_vlr)
        for i in cont:
            if cont[i]==m_valor:
                lista_key+=[i]
        lista_final+=sorted(lista_key)
        
        for i in lista_final:
                if i in cont:
                    del(cont[i])
        lista_key,lista_vlr,cont_1=[],[],0   
    
    if list(s_c)[1:6]!=lista_final[0:5]:
        return False
    return True

#3.3 filtrar_bdb
def filtrar_bdb(entradas):
    '''Função que devolve uma lista de entradas da bdb e, depois de filtrar as
    que cuja sequência de controlo não á coerente com a cifra,
    apresenta apenas as entradas erradas.
    -Input de uma lista de entradas -entradas.
    -Devolve uma lista apenas com as entradas erradas -lista_filtrada
   filtrar_bdb: lista--->lista
    '''
    if type (entradas)!=list or entradas==[]:
        raise ValueError('filtrar_bdb: argumento invalido')
    for i in entradas:
        if eh_entrada(i)==False:
            raise ValueError('filtrar_bdb: argumento invalido')
    lista_filtrada=[]
    for i in entradas:
        if validar_cifra(i[0],i[1])==False:
            lista_filtrada+=[i]
    return lista_filtrada



#4.2  obter num seguranca
def obter_num_seguranca(x):
    '''Fução que devolve à menor diferenca positive entre dois números.
    -Input de um tuple constituido de números inteiros positivos -x.
    -Devolve um inteiro correspondente à menor diferenca positiva entre dois
    elementos do tuple -nr.
    obter_num_seguranca: tuplo ---> inteiro
    '''
    nr=abs(x[0]-x[len(x)-1])
  #linha para atribuir um valor inical antes do ciclo para o nr
  # foi atribuido arbitrariamente a diferença entre o primeiro e último elemento 
  #se algum for mais pequeno então vai trocar, se não, fica igual
  
    for i in x:
        for y in range (0,len(x)):
            if abs(i-x[y])!=0:
                diferenca= abs(i-x[y])
                if diferenca<nr :
                    nr=diferenca
                    #ciclo para atribuir a nr a menor diferenca
    return nr


#4.3 decifrar_texto 
def decifrar_texto(cifra,s_seguranca):
    '''Função que recebe uma cifra e o número de seguranca e devolve o texto 
    decifrado.
    -Input de uma string que será a cifra -cifra- e de um inteiro que será 
    o número de seguranca-s_seguranca
    -Devolve uma string que corresponde ao texto decifrado-string
    decifrar_texto: cad. carateres x inteiro ---> cad. carateres
    '''
    list_cifra=list(cifra)
    string=''
    len_cifra=len(list_cifra)
  
    for i in range (len_cifra):
        ord_cifra= ord(list_cifra[i])
        if i%2==0 and ord_cifra!=45:
            avancar = s_seguranca+1
            avancar+=ord_cifra
        elif i%2!=0 and ord_cifra!=45:
            avancar = s_seguranca-1
            avancar+=ord_cifra
        elif ord_cifra==45:
            avancar=32
  
        if avancar>122:
            avancar=avancar-122
            avancar=avancar%26
            avancar +=96
        
        
        string+=chr(avancar)
    
    return string

#4.4 decifrar_bdb
def decifrar_bdb(bdb):
    '''Função que devolve o texto das entradas da bdb decifrado.
    -Input de uma lista com as entradas da bdb-bdb
    -Devolve uma lista com o texto decifrado -res
    decifrar_bdb: lista--->lista
    '''
    if type(bdb)!=list or bdb==[]:
        raise ValueError ('decifrar_bdb: argumento invalido')
    res=[]
    for i in bdb:
        if eh_entrada(i)== False:
            raise ValueError ('decifrar_bdb: argumento invalido')
        else:
            nr_seguranca= obter_num_seguranca(i[2])
            res+= [decifrar_texto(i[0],nr_seguranca)]
    return res
    
 #5.1 eh_utilizador 
def eh_utilizador (user_info):
    '''Função que devolve o valor booleano de um argumento em relação a este
    ser uma entrada da bdb.
    -Input de um argumento de qualquer tipo, universal -user_info
    -Devolve um valor booleano -True ou False
    eh_utilizador: universal--->booleano
    '''
    if type(user_info)!=dict or len(user_info)!=3:
        return False
    if 'name' not in user_info or 'pass' not in user_info or \
       'rule' not in user_info:
        return False
    rule_v=user_info['rule']
    if 'vals' not in rule_v or 'char' not in rule_v or len(rule_v)!=2:
        return False
    #linhas para confirmar que estão todos os componentes
    if type(user_info['name'])!=str or type(user_info['pass'])!=str:
        return False
    if len(user_info['name'])<1 or len(user_info['pass'])<1:
        return False
    #avaliar name e pass
    if type(rule_v['vals'])!=tuple or len(rule_v['vals'])!=2:
        return False
    for i in rule_v['vals']:
        if i<0:
            return False
    if rule_v['vals'][0] > rule_v['vals'][1]:
        return False
            
    if type(rule_v['char'])!=str or len(rule_v['char'])!=1:
        return False
    if ord(rule_v['char'])<97 or ord(rule_v['char'])>122:
        return False
    #avaliar parte da rule
    
    return True
    

#5.2 eh_senha_valida 
def eh_senha_valida(senha,rule):
    '''Função que devolve o valor booleano em relação a uma pass, cumprir ambas
    as regras gerais como individuais da bdb
    -Input de uma string-senha- e de um dicionário que será a 
    regra individual-rule
    -Devolve um valor booleano- True ou False
    eh_senha_valida: cad.carateres x dicionário---> booleano
    '''
    #confimar regras gerais
    #regra de pelo menos 3 letras serem vogais
    vogais_min=('a','e','i','o','u')
    cont_v_min=0
    for letra in senha:
        if letra in vogais_min:
            cont_v_min+=1
    if cont_v_min<3:
        return False
    #verificacao da regra de ter pelo menos um carater repetido consecutivo
    cont_cc=0
    for i in range(0,len(senha)-1):
        if ord(senha[i])== ord(senha[i+1]):
            cont_cc+=1
    if cont_cc<1:
        return False
    #verificação das regras individuais
    cont_letra=0
    for letra in senha:
        if ord(letra)==ord(rule['char']):
            cont_letra+=1
    if rule['vals'][1]<cont_letra or cont_letra<rule['vals'][0]:
        return False
    return True

#5.3 filtar_senhas 
def filtrar_senhas(bdb):
    '''Funcao que filtra os 'name' que não cumprem as regras, ou seja que
    estão erradas, por ordem alfabética
    -Input de uma lista que integra um ou mais dicionários que correspondem
    as entradas das bdb -bdb
    -Devolve uma lista com os 'name', por ordem alfabética,
    que têm senhas erradas- new_list
    filrar_senhas: lista--->lista
    '''
    #validação do argumento
    if type(bdb)!=list or bdb==[]:
        raise ValueError('filtrar_senhas: argumento invalido')
    for i in bdb:
        if eh_utilizador(i)==False:
            raise ValueError('filtrar_senhas: argumento invalido')
    #filtragem das senhas certas
    new_list=[]
    for i in bdb:
        if eh_senha_valida(i['pass'],i['rule'])==False:
            new_list+=[i['name']]
    return sorted(new_list)