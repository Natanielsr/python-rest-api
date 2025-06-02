curl -X POST "http://localhost:5000/slides/generate/" \
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