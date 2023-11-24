IMPORTANTE

Para executar o script precisa definir o PYTHONPATH, para isso, apenas set este comando 
no terminal, ele irá definir a variável pythonpath apenas na sessão atual:

windows:
    set PYTHONPATH=C:\caminho\para\seu\diretorio

Linux:
    export PYTHONPATH=/caminho/para/seu/diretorio

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Como a estrutura do código foi pensado?


1. Organização do código:

    O código é totalmente orientado a objetos. Para organizar os dados, foi criado objetos
    que estão localizados no pasta models. 

    Em JavaScript, quase tudo é objeto. Pensando nisso, percebe-se que JSON (JavaScript Object Notation), possui uma estrutura muito similar a estrutura dos objetos literais no JS. 

    Exemplo:

        Object {
            chave : valor
        }

    Se eu fizer um parser do JSON para JavaScript ele me dirá quais são objetos e quais são
    "atributos" do objeto.

    Foi pensando exatamente assim que decidi que tudo que for um objeto no JS, será um model. Como os dados que precisava ficam dentro de Match da lista de objetos matches, decidi começar
    por ele. Stadium, Team e Goal, também são objetos que contém informações. 

    Por isso cheguei a conclusão:
        -> Goal
        -> Match
        -> Stadium
        -> Team

    Serão meus models e conterão os dados. Vou organizá-los exatamente como está no JSON.
    Se Match contém Team que é outro objeto, então um dos atributos de Match, será Team.

    Após configurar o arquivo ini, criar classe para leitura e conexão com a API, decidimos criar duas funções localizadas na pasta data_processing, nela tenho uma classe para carregar todos
    os dados em memória, uma classe para criar os objetos e outra para manipulá-los. 

    Para gerar as repostas, creio que não foi o "melhor jeito" pensado para realizar a busca.
    Eu utilizo a função getattr que busca o valor de um atributo armazenado no objeto. Se o valor
    for do atributo do objeto for igual ao valor que estou procurando, então é armazenado em uma 
    nova lista, lançado para uma outra classe que irá percorrer o resulado. 