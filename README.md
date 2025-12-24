# Word MCP Server

Word MCP Server es una aplicacion Python que permite crear y editar documentos Microsoft Word (.docx) a traves de API. Este proyecto utiliza FastMCP para construir herramientas de interaccion con documentos Word.

## Instalacion

### Requisitos

- Python 3.12+
- Bibliotecas dependientes:
  - python-docx
  - opencv-python (cv2)
  - numpy
  - FastMCP

### Instalar bibliotecas
```bash
uv venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
uv pip install .
```

## Caracteristicas

Word MCP Server proporciona herramientas para:

1. Crear y abrir documentos Word
2. Agregar y formatear texto
3. Agregar imagenes
4. Crear tablas
5. Gestionar recursos y prompts

## Guia de uso

### Configuracion e inicio con LLM

Para usar Word MCP Server con modelos de lenguaje grande (LLM), necesitas configurar a traves de un archivo JSON:

```json
{
  "mcpServers": {
    "word-mcp-server": {
      "command": "C:/ruta/a/word-mcp-server/.venv/Scripts/python.exe",
      "args": ["C:/ruta/a/word-mcp-server/server.py"]
    }
  }
}
```

#### Explicacion de la configuracion:

- `mcpServers`: Objeto que contiene la configuracion de los MCP servers
- `word-mcp-server`: Nombre identificador del servidor
- `command`: Ruta al interprete Python (generalmente en el entorno virtual)
- `args`: Parametros de linea de comandos, el primer parametro es la ruta al archivo server.py


## El servidor se iniciara y estara listo para recibir comandos del LLM

#### Interaccion con LLM:

Una vez configurado e iniciado exitosamente, puedes usar el LLM para:
- Crear y editar documentos Word mediante comandos en lenguaje natural
- Generar contenido automaticamente basado en prompts
- Formatear texto, agregar imagenes y tablas de manera inteligente

### Crear nuevo documento

```python
create_new_document()
```

### Abrir documento existente

```python
open_document("ruta/al/documento.docx")
```

### Agregar titulos y parrafos

```python
# Agregar titulo
add_heading("Titulo del documento", level=0)
add_heading("Capitulo 1", level=1)

# Agregar parrafo de texto
add_paragraph("Este es el contenido del parrafo.")

# Agregar parrafo con formato
add_paragraph(
    "Este es un parrafo con formato.",
    style="Normal",
    font_size=14,
    bold=True,
    italic=False,
    alignment=WD_PARAGRAPH_ALIGNMENT.CENTER
)
```

### Agregar formato a una parte del texto

```python
# Crear parrafo
p = add_paragraph("Este es un parrafo basico. ")

# Agregar parte de texto con diferente formato
add_run_to_paragraph(
    p,
    "Esta parte esta en negrita y rojo.",
    bold=True,
    color="red"
)

# Agregar parte de texto con resaltado
add_run_to_paragraph(
    p,
    " Esta parte tiene resaltado amarillo.",
    highlight="yellow"
)
```

### Agregar imagen

```python
# Agregar imagen desde ruta de archivo
add_picture("ruta/a/imagen.jpg", width=4.0)

# O agregar imagen desde matriz numpy
import numpy as np
import cv2

img = cv2.imread("ruta/a/imagen.jpg")
add_picture(img, width=3.5)
```

### Crear tabla

```python
# Crear tabla con 3 filas y 4 columnas
table = add_table(rows=3, cols=4, style="Table Grid")

# Llenar datos en la tabla
table.cell(0, 0).text = "Fila 1, Columna 1"
table.cell(0, 1).text = "Fila 1, Columna 2"
# ...
```

## Colores soportados

Al usar los parametros `color` y `highlight`, puedes usar los siguientes valores:

- black
- blue
- green
- dark blue
- dark red
- dark yellow
- dark green
- pink
- red
- white
- teal
- yellow
- violet
- gray25
- gray50

## Notas

- Este proyecto usa la biblioteca `python-docx` para interactuar con documentos Word
- Los recursos y prompts se almacenan en los directorios `resources` y `prompts`
- Asegurate de haber instalado todas las bibliotecas dependientes antes de ejecutar el servidor

## Ejemplo completo

```python
# Crear nuevo documento
create_new_document()

# Agregar titulo
add_heading("Informe del proyecto", level=0)

# Agregar informacion del creador
p = add_paragraph("Creador: ")
add_run_to_paragraph(p, "Juan Perez", bold=True)

# Agregar indice
add_heading("Indice", level=1)
add_paragraph("1. Introduccion")
add_paragraph("2. Contenido")
add_paragraph("3. Conclusion")

# Agregar contenido
add_heading("1. Introduccion", level=1)
add_paragraph("Esta es la introduccion del proyecto...")

# Agregar imagen
add_paragraph("Imagen ilustrativa:")
add_picture("diagrama_proyecto.jpg", width=5.0)

# Agregar tabla de datos
add_heading("Tabla de datos", level=2)
table = add_table(rows=3, cols=3)
table.cell(0, 0).text = "Dato 1"
table.cell(0, 1).text = "Dato 2"
table.cell(0, 2).text = "Dato 3"
# Llenar otros datos...

# Guardar documento
save_document("informe_proyecto.docx")
```
