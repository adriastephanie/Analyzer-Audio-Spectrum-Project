# Analyzer-Audio-Spectrum-Project

Projeto para aula de Comunicação de Dados! 

## Passo a passo

- Rodar arquivo para começar a gravação
- Converter o arquivo
- Rodar o arquivo que gera a analise dos gráficos
## Como Rodar

Primeiramente, deve excluir dados "outputadria.wav" e "stereo.wav"  

Para começar a gravar, deve ser rodar o arquivo sa.py

Para converter o audio deve rodar o comando:

```sh
ffmpeg -i outputadria.wav -ac 2 stereo.wav
```

Para começar gerar os gráficos, deve ser rodar o arquivo analise.py 

## License

MIT

**Free Software, Hell Yeah!**
