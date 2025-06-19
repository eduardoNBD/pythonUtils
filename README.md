# Utilidades de Python

Este repositorio contiene una colección de scripts de Python para realizar diversas tareas útiles.

## Scripts Disponibles

### Generador de Códigos QR (`QrGenerator.py`)

Este script genera códigos QR a partir de un texto o URL proporcionado por el usuario. Utiliza la biblioteca `qrcode` y guarda la imagen del código QR en un archivo.

### Corrector Ortográfico (`OrthographyCorrection.py`)

Un script que utiliza la biblioteca `autocorrect` para corregir la ortografía de un texto en español.

### Abridor de Carpetas (`OpenFolders.py`)

Una utilidad simple para abrir directorios predefinidos del sistema de forma automática.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias. Puedes instalarlas usando pip:

```bash
pip install qrcode[pil]
pip install autocorrect
pip install openai
```

*(Nota: Las dependencias `bs4`, `diffusers`, `transformers`, `accelerate`, `scipy`, y `safetensors` también estaban listadas pero no parecen corresponder directamente con los scripts principales. Se han omitido de la lista principal pero puedes instalarlas si son necesarias para alguna funcionalidad no evidente).*