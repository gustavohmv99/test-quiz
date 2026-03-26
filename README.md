[![tests](https://github.com/andrehora/test-quiz/actions/workflows/tests.yml/badge.svg)](https://github.com/andrehora/test-quiz/actions/workflows/tests.yml) 

# Testing Quiz

Neste exercício, iremos melhorar os testes de unidade de sistema de quiz.
Você deve realizar os 3 commits descritos abaixo e submeter os 3 links dos commits via Moodle.

### Overview

Primeiramente, explore o código do sistema em [model.py](https://github.com/andrehora/test-quiz/blob/main/model.py).
Note que temos duas classes: `Question` (que representa as questões do quiz) e `Choice` (escolha das questões).

Explore também os cinco testes em [tests.py](https://github.com/andrehora/test-quiz/blob/main/tests.py) para entender melhor como o sistema funciona:
Por exemplo:

```python
def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

...
```

Você deve realizar os 3 commits descritos abaixo e submeter os 3 links dos commits via Moodle.

# Commit 1: Running the tests

Antes de iniciar as atividades de teste, precisamos configurar o repositório de trabalho.

### Crie um fork deste repositório

Primeiramente, crie um fork deste repositório.
Para isso, basta clicar no botão `Fork` no canto superior direito.
Caso tenha dúvidas, verifique a documentação do GitHub sobre como [criar fork de um repositório](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

### Ative o GitHub Actions para rodar os testes a cada commit

Neste projeto, utilizamos o [GitHub Actions](https://github.com/features/actions) (ferramenta de CI/CD do GitHub) para executar os testes automaticamente a cada commit.

Abra o arquivo de configuração do GitHub Actions [.github/workflows/tests.yml](https://github.com/andrehora/test-quiz/blob/main/.github/workflows/tests.yml) e observe que os testes são executados em três sistemas operacionais (Ubuntu, macOS e Windows) e múltiplas versões da linguagem Python.
Veja um exemplo da execução em: https://github.com/andrehora/test-quiz/actions/runs/14231638679.

Ative o GitHub Actions no seu repositório.
Para isso, basta ir na aba `Actions` e clicar no botão verde.

### Clone o seu repositório

Em seguida, clone o seu repositório para uma pasta local e entre na pasta:

```
$ git clone https://github.com/<SEU-USUARIO>/quiz
$ cd quiz
```

### Instale o pytest

> [!NOTE]
> Antes de instalar a ferramenta, é recomendado criar e ativar um [ambiente virtual Python](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments).

Nossos testes utilizam o framework de testes [pytest](https://docs.pytest.org).
Instale o pytest:

```
$ pip install pytest
```

### Rode os testes localmente

Para executar os testes localmente, basta rodar o comando `pytest -v tests.py`:

```
$ pytest -v tests.py
========================================== test session starts ===========================================
...                                                                                     
tests.py::test_create_question PASSED                                                              [ 20%]
tests.py::test_create_multiple_questions PASSED                                                    [ 40%]
tests.py::test_create_question_with_invalid_title PASSED                                           [ 60%]
tests.py::test_create_question_with_valid_points PASSED                                            [ 80%]
tests.py::test_create_choice PASSED                                                                [100%]
=========================================== 5 passed in 0.01s ============================================
```

### Faça o commit para executar os testes remotamente (via GitHub Actions)

Os testes serão executados automaticamente no GitHub Actions sempre que um commit é realizado.
Portanto, para rodar os testes no GitHub Actions, realize uma alteração qualquer neste arquivo `README.md` e faça o commit da alteração com a seguinte mensagem: `Commit 1: Running the tests`.

Em seguida, clique na aba `Actions` e veja que os testes foram executados com sucesso no GitHub Actions. 
Observe as execuções em múltiplos sistemas operacionais (Ubuntu, macOS e Windows) e versões da linguagem Python.

# Commit 2: Creating 10 unit tests

Crie mais dez testes de unidade no arquivo `tests.py`.
Utilize boas práticas, tais como (1) testar comportamentos, não métodos, (2) testar através de APIs públicas e (3) criar testes pequenos e focados.

Rode os testes localmente com o comando `pytest -v tests.py`.
Só faça o commit com os testes passando.

### Faça o commit
Com os testes passando, faça o commit com a seguinte mensagem: `Commit 2: Creating 10 unit tests`.

# Commit 3: Testing with fixtures

Crie pelo menos mais dois testes de unidade utilizando as [fixtures do pytest](https://docs.pytest.org/en/stable/explanation/fixtures.html).
Por exemplo, você pode incluir na fixture uma questão com múltiplas escolhas, e esta questão será reutilizada nos testes.

Um exemplo simples do uso fixtures pode ser visto abaixo:

```python
@pytest.fixture
def data():
    return [1,2,3]

def test_sum(data):
    assert sum(data) == 6

def test_max(data):
    assert max(data) == 3

def test_in(data):
    assert 1 in data
```

### Faça o commit
Com os testes passando, faça o commit com a seguinte mensagem: `Commit 3: Testing with fixtures`.
