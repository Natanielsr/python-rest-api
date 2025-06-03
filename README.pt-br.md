### 📌 **Python REST API**

Esta é a documentação da API `python-rest-api`, contendo endpoints para busca de músicas, geração de slides e obtenção de letras de músicas.

Youtube Video 👉
[![Watch video on YouTube](https://img.youtube.com/vi/ibtcd_vtW9A/0.jpg)](https://www.youtube.com/watch?v=ibtcd_vtW9A)

## 🚀 **Endpoints**

### 🔍 **Buscar Músicas**  
**GET** `{{domain}}/search/{termo}`  

**Exemplo:**  
```sh
curl -X GET "{{domain}}/search/mãe do emanuel"
```

**Exemplo de Resposta:**
```json
{
    "results": [
        {
            "link": "https://www.letras.mus.br/amor-e-missao/mae-do-emanuel/",
            "name": "Mãe do Emanuel - Amor e Missão"
        },
        {
            "link": "https://www.letras.mus.br/heber-campos/mae-do-emanuel/",
            "name": "Mãe do Emanuel - Heber Campos"
        }
    ]
}
```

---

### 💑 **Gerar Slides**  
**POST** `{{domain}}/slides/generate/`  

**Body (JSON):**  
```json
{
    "params": [
        {
            "name": "entrada",
            "link": "https://musicasparamissa.com.br/musica/nos-te-louvamos-juliana-de-paula/"
        },
        {
            "name": "Santo",
            "link": "https://musicasparamissa.com.br/musica/santo-leo-mantovani/"
        },
        {
            "name": "Gloria",
            "link": "https://www.letras.mus.br/agnus-dei/901672/"
        }
    ]
}
```

**Exemplo:**  
```sh
curl -X POST "{{domain}}/slides/generate/" \
     -H "Content-Type: application/json" \
     -d '{
        "params": [
            {
                "name": "entrada",
                "link": "https://musicasparamissa.com.br/musica/nos-te-louvamos-juliana-de-paula/"
            },
            {
                "name": "Santo",
                "link": "https://musicasparamissa.com.br/musica/santo-leo-mantovani/"
            },
            {
                "name": "Gloria",
                "link": "https://www.letras.mus.br/agnus-dei/901672/"
            }
        ]
    }'
```

**Exemplo de Resposta:**
```json
{
    "file_name": "6caca7fe49f846bfbe1d144e0f5aba2c.pptx",
    "file_url": "{{domain}}/slides/download/6caca7fe49f846bfbe1d144e0f5aba2c.pptx",
    "message": "Slides generated successfully"
}
```

---

### 🎵 **Obter Letra de Música**  
**GET** `{{domain}}/lyric/{url}`  

**Exemplo:**  
```sh
curl -X GET "{{domain}}/lyric/https://www.letras.mus.br/queen/64295/"
```

**Exemplo de Resposta:**
```json
{
    "lyric": "Is this the real life?\nIs this just fantasy?\nCaught in a landslide\nNo escape from reality\n\nOpen your eyes\nLook up to the skies and see\nI'm just a poor boy\nI need no sympathy\nBecause I'm easy come, easy go\nLittle high, little low\nAnyway the wind blows\nDoesn't really matter to me\nTo me"
}
```

---

### 📌 **Observações**
- Substitua `{{domain}}` pelo domínio da API.
- Os endpoints não requerem autenticação.
- Certifique-se de enviar o JSON corretamente formatado ao fazer requisições `POST`.
- Variáveis ​​de ambiente necessárias:
  - `GOOGLE_SEARCH_API_KEY`
  - `GOOGLE_SEARCH_ENGINE_ID`

  Para criar um ambiente virtual (venv) no Python e instalar as dependências de um arquivo `requirements.txt`, siga os passos abaixo:

---

### 🧪 **1. Criar o ambiente virtual (venv)**

Abra o terminal e navegue até a pasta do seu projeto:

```bash
cd /caminho/para/seu/projeto
```

Então, crie o ambiente virtual com:

```bash
python -m venv venv
```

> Isso criará uma pasta chamada `venv` com o ambiente isolado.

---

### 🔄 **2. Ativar o ambiente virtual**

* **No Windows:**

```bash
venv\Scripts\activate
```

* **No Linux/macOS:**

```bash
source venv/bin/activate
```

> Quando ativado, o terminal vai mostrar o nome do ambiente no início da linha, algo como: `(venv)`

---

### 📦 **3. Instalar os requirements**

Depois de ativar o ambiente, use o `pip` para instalar as dependências:

```bash
pip install -r requirements.txt
```

---

### ✅ Dica final

Para garantir que está usando o `pip` do ambiente virtual, você pode verificar com:

```bash
which pip     # Linux/macOS
where pip     # Windows
```

---



