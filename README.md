# Projeto de Automação com Selenium — Buscando Documentação SQLAlchemy

Este é um projeto simples de automação de navegador utilizando **Selenium** com Python. A ideia foi bem simples: Executar uma pesquisa no google e abrir o resultado.

O objetivo principal foi aprender e praticar os conceitos de automação web com Selenium, aplicando boas práticas como:
- Separação de responsabilidades em arquivos (`main.py`, `options.py`, `waiters.py`)
- Tipagensm, incluindo especificas como `WebDriver`, `WebElement`
- Esperas explícitas com `WebDriverWait`, definindo uma função própria pra isso
- Técnicas anti-detecção de bot

---

## O que esse script faz

1. Abre o Google Chrome com configurações especiais que disfarçam a automação.
2. Acessa o site [google.com](https://google.com).
3. Busca por `"SQLAlchemy Documentation"`.
4. Aguarda o link correto aparecer e clica nele.
5. Aguarda 10 segundos para visualização e fecha o navegador.

---

## Explicação Técnica e Comentada

### `main.py`

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
```

- `webdriver`: É o núcleo do Selenium, responsável por controlar o navegador.
- `Service`: Utilizado para informar o caminho do `chromedriver`.
- `By`: Utilizado para localizar elementos na página (por ID, classe, texto, etc).
- `Keys`: Permite usar teclas do teclado como `ENTER`.

---

```python
from options import options
from waiters import wait_for_element
```

- `options.py`: Contém configurações personalizadas para o Chrome.
- `waiters.py`: Função utilitária que aguarda elementos carregarem na tela.

---

```python
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"
})
```

- Isso engana sites que tentam detectar bots com `navigator.webdriver`. Define esse valor como `undefined`, simulando um navegador humano.

---

```python
driver.get("https://google.com")
```

- Acessa a URL informada.

---

```python
wait_for_element(driver, By.CLASS_NAME, "gLFyf", 5)
```

- Espera até o campo de busca do Google carregar completamente antes de interagir.

---

```python
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("SQLAlchemy Documentation" + Keys.ENTER)
```

- Encontra o input e envia o texto + tecla ENTER para fazer a busca.

---

```python
wait_for_element(driver, By.PARTIAL_LINK_TEXT, "SQLAlchemy Documentation", 5)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "SQLAlchemy Documentation")
link.click()
```

- Aguarda o link da documentação aparecer nos resultados e clica nele.

---

```python
import time
time.sleep(10)
```

- Espera 10 segundos antes de encerrar o navegador, apenas para visualização da página final.

---

```python
driver.quit()
```

- Fecha o navegador e encerra o script.

---

## Estrutura de Arquivos

```
selenium-doc-search/
│
├── main.py            # Lógica principal da automação
├── options.py         # Configurações do Chrome para disfarçar a automação
├── waiters.py         # Função utilitária para espera de elementos
├── chromedriver.exe   # Driver do Chrome (você precisa baixar e manter atualizado)
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo
```

---

## Requisitos

- Python 3.10+
- Google Chrome instalado
- [Chromedriver](https://chromedriver.chromium.org/) compatível com sua versão do Chrome

---

## Instalando as dependências

```bash
pip install -r requirements.txt
```

---

## Como rodar

```bash
python main.py
```

Você verá o navegador abrindo, buscando no Google, acessando a documentação do SQLAlchemy, aguardando 10 segundos, e depois fechando.

---

## Alguns Aprendizados
- Esperar elementos de forma explícita é mais confiável do que usar `sleep` para interações.
- O Selenium pode ser detectado por sites — mas dá pra contornar isso.
- Ler a documentação e testar na prática é a melhor forma de aprender.

---

## Tecnologias utilizadas

- Python 3
- Selenium 4
- Google Chrome + ChromeDriver

---

## Próximos passos
- Fazer pesquisas utilizando técnicas de OSINT

---

