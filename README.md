# YOLO-Object-Detection

Este projeto implementa um sistema de detecção de objetos usando a arquitetura YOLO (You Only Look Once), permitindo a detecção em tempo real de objetos em imagens e vídeos.

## Visão Geral do Projeto

O projeto utiliza o framework Darknet para implementar a detecção de objetos YOLO, com suporte opcional a GPU através do CUDA para melhor performance. O sistema inclui ferramentas para rotulação de dados, treinamento do modelo e inferência.

## Componentes do Sistema

O sistema possui quatro componentes principais:

1. **Preparação dos Dados**
   - Rotulação inicial das imagens usando LabelMe
   - Conversão dos arquivos JSON para formato YOLO
   - Organização dos dados em diretórios específicos

2. **Configurações do Projeto**
   - Arquivos de configuração para treinamento
   - Modelo base YOLOv4 para transferência de aprendizado

3. **Treinamento do Modelo**
   - Uso do framework Darknet para o processo de treinamento
   - Integração com CUDA para aceleração em GPU (opcional)

4. **Detecção de Objetos**
   - Utilização do modelo treinado para detecção em novas imagens


## Pré-requisitos

* Darknet (framework principal)
* CUDA (opcional, para GPUs NVIDIA)
* Python com dependências:
```bash
pip install numpy opencv-python
```

## Instalação

1. Clonar o repositório:
```bash
git clone https://github.com/seu-usuario/YOLO-Object-Detection.git
```
2. Instalar dependências Python:
```bash
pip install -r requirements.txt
```

## Uso

### Rotulação de Dados

1. Abra o LabelMe e rotule suas imagens
2. Execute o script de conversão:
```bash
python script/convert_json_to_yolo.py --dir caminho_das_imagens
```

### Treinamento

1. Configure os arquivos em `cfg/`:
   - `obj.data`: configurações do dataset
   - `yolo-obj.cfg`: parâmetros da rede
2. Execute o treinamento:
```bash
./darknet detector train cfg/obj.data cfg/yolo-obj.cfg yolov4.conv.137 -dont_show -map
```

### Detecção

Para realizar detecção em uma imagem:
```bash
./darknet detector test cfg/obj.data cfg/yolo-obj.cfg backup/yolov4-custom_last.weights -thresh 0.25 caminho_imagem.jpg
```

## Detalhes Técnicos

* O modelo utiliza YOLOv4 como base, que alcança 55.8% AP no conjunto de dados COCO test-dev
* Com CUDA habilitado, o treinamento é significativamente acelerado
* O sistema suporta detecção em tempo real com performance otimizada
