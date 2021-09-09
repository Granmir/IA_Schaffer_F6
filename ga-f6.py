import numpy as np
import matplotlib.pyplot as plt
import functions as f
import bitstring as bts
import binstr as bs

#Parâmentros
#(-100 a 100)
gen = 100
bits = 25
preci = 5
inter = [-100, 100]
popTam = 100
mut = 0.01
cruz = 0.7
melhores = np.array(())
media = np.array(())
piores = np.array(())

esco = [2, 4, 6, 100, 101, 102, 192, 193, 194, 0]
path = 'data/'

#Geração da população inicial
pop = f.popIni(bits*2, popTam)

for i in range(gen):
    #Converte a popução para real
    popReal = f.bin2real(pop, inter, bits, preci)

    #Avaliação
    fit = f.f6(popReal[0], popReal[1])
    #Seleciona os melhores e a média
    melhores = np.append(melhores, max(fit))
    media = np.append(media, np.mean(fit))
    piores = np.append(piores, min(fit))
    #Salvando a população para a exibição
    if i == esco[0]:
        np.save(path+'pop-%i.npy' %(i), popReal)
        np.save(path+'fit-%i' %(i), fit)
        esco = esco[1:]

    #Seleção e cruzamento
    pop = f.selecaoRoleta(pop, fit, cruz)

    #Mutação
    pop = f.mutacao(pop, mut)

    #Converte a pop para inteiro
    pop = pop.astype(int)


#Etapa para salvar o último indivíduo
#Converte a popução para real
popReal = f.bin2real(pop, inter, bits, preci)

#Avaliação
fit = f.f6(popReal[0], popReal[1])
#Seleciona os melhores
melhores = np.append(melhores, max(fit))
media = np.append(media, np.mean(fit))
piores = np.append(piores, min(fit))

plt.plot(melhores, label='Melhor')
plt.plot(media, 'o', label='Média')
plt.plot(piores, label='Piores')
plt.xlabel('Geracoes')
plt.ylabel('f6')
plt.show()
