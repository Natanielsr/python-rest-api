### 📌 **Python REST API**

Esta é a documentação da API `python-rest-api`, contendo endpoints para busca de músicas, geração de slides e obtenção de letras de músicas.

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
    "file_url": "https://web-production-594d.up.railway.app/slides/download/6caca7fe49f846bfbe1d144e0f5aba2c.pptx",
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

