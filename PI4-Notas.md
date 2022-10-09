# Links

    - https://medium.com/analytics-vidhya/tf-idf-term-frequency-technique-easiest-explanation-for-text-classification-in-nlp-with-code-8ca3912e58c3
    - https://www.computersciencemaster.com.br/como-implementar-o-tf-idf-em-python/
    - https://towardsdatascience.com/tf-idf-explained-and-python-sklearn-implementation-b020c5e83275
    - https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
    - https://www.freecodecamp.org/news/python-lowercase-how-to-use-the-string-lower-function/


# Conceitos

Term-Frequency (TF): Frequência da palavra no documento atual, onde TF = (número de vezes que o termo "T" aparece no documento atual) / (número de termos do documento) . É um cálculo local.

Inverse Document Frequency (IDF): É o quão rara é a palavra em todos os documentos, onde IDF = log(N/n), em que "N" é o número total de documentos e "n" é o número onde o termo apareceu. É um cálculo global.

TF-IDF: É a importância de uma palavra para um documento em uma coleção ou corpo. TF-IDF = TF * IDF