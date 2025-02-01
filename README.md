### 📌 **Python REST API**

📌 [🇬🇧 English Version](README.md)  
📌 [🇧🇷 Versão em Português](README.pt-br.md)  

This is the documentation for the `python-rest-api`, containing endpoints for searching music, generating slides, and retrieving song lyrics.

## 🚀 **Endpoints**

### 🔍 **Search Music**  
**GET** `{{domain}}/search/{term}`  

**Example:**  
```sh
curl -X GET "{{domain}}/search/mãe do emanuel"
```

**Example Response:**
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

### 💑 **Generate Slides**  
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

**Example:**  
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

**Example Response:**
```json
{
    "file_name": "6caca7fe49f846bfbe1d144e0f5aba2c.pptx",
    "file_url": "{{domain}}/slides/download/6caca7fe49f846bfbe1d144e0f5aba2c.pptx",
    "message": "Slides generated successfully"
}
```

---

### 🎵 **Get Song Lyrics**  
**GET** `{{domain}}/lyric/{url}`  

**Example:**  
```sh
curl -X GET "{{domain}}/lyric/https://www.letras.mus.br/queen/64295/"
```

**Example Response:**
```json
{
    "lyric": "Is this the real life?\nIs this just fantasy?\nCaught in a landslide\nNo escape from reality\n\nOpen your eyes\nLook up to the skies and see\nI'm just a poor boy\nI need no sympathy\nBecause I'm easy come, easy go\nLittle high, little low\nAnyway the wind blows\nDoesn't really matter to me\nTo me"
}
```

---

### 📌 **Notes**
- Replace `{{domain}}` with the actual API domain.
- The endpoints do not require authentication.
- Ensure you send correctly formatted JSON when making `POST` requests.

