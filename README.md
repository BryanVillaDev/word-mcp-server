# Word MCP Server

Word MCP Server là một ứng dụng Python cho phép tạo và chỉnh sửa tài liệu Microsoft Word (.docx) thông qua API. Dự án này sử dụng FastMCP để xây dựng các công cụ tương tác với tài liệu Word.

## Cài đặt

### Yêu cầu

- Python 3.12+
- Các thư viện phụ thuộc:
  - python-docx
  - opencv-python (cv2)
  - numpy
  - FastMCP

### Cài đặt thư viện
```bash
uv venv
source venv/bin/activate
uv pip install .
```

## Tính năng

Word MCP Server cung cấp các công cụ để:

1. Tạo và mở tài liệu Word
2. Thêm và định dạng văn bản
3. Thêm hình ảnh
4. Tạo bảng
5. Quản lý tài nguyên và prompt

## Hướng dẫn sử dụng

### Cấu hình và khởi chạy với LLM

Để sử dụng Word MCP Server với các mô hình ngôn ngữ lớn (LLM), bạn cần cấu hình thông qua file JSON:

```json
{
  "mcpServers": {
    "word-mcp-server": {
      "command": "/path/to/word-mcp-server/.venv/bin/python3",
      "args": ["/path/to/word-mcp-server/server.py"]
    }
  }
}
```

#### Giải thích cấu hình:

- `mcpServers`: Object chứa cấu hình cho các MCP server
- `word-mcp-server`: Tên định danh của server
- `command`: Đường dẫn đến Python interpreter (thường nằm trong môi trường ảo)
- `args`: Các tham số dòng lệnh, trong đó tham số đầu tiên là đường dẫn đến file server.py


## Server sẽ khởi động và sẵn sàng nhận lệnh từ LLM

#### Tương tác với LLM:

Khi đã cấu hình và khởi chạy thành công, bạn có thể sử dụng LLM để:
- Tạo và chỉnh sửa tài liệu Word thông qua lệnh tự nhiên
- Tự động tạo nội dung dựa trên prompt
- Định dạng văn bản, thêm hình ảnh và bảng một cách thông minh

### Tạo tài liệu mới

```python
create_new_document()
```

### Mở tài liệu có sẵn

```python
open_document("path/to/document.docx")
```

### Thêm tiêu đề và đoạn văn

```python
# Thêm tiêu đề
add_heading("Tiêu đề tài liệu", level=0)
add_heading("Chương 1", level=1)

# Thêm đoạn văn bản
add_paragraph("Đây là nội dung đoạn văn bản.")

# Thêm đoạn văn bản với định dạng
add_paragraph(
    "Đây là đoạn văn bản được định dạng.",
    style="Normal",
    font_size=14,
    bold=True,
    italic=False,
    alignment=WD_PARAGRAPH_ALIGNMENT.CENTER
)
```

### Thêm định dạng cho một phần văn bản

```python
# Tạo đoạn văn bản
p = add_paragraph("Đây là đoạn văn bản cơ bản. ")

# Thêm phần văn bản có định dạng khác
add_run_to_paragraph(
    p,
    "Phần này được in đậm và màu đỏ.",
    bold=True,
    color="red"
)

# Thêm phần văn bản có highlight
add_run_to_paragraph(
    p,
    " Phần này được highlight màu vàng.",
    highlight="yellow"
)
```

### Thêm hình ảnh

```python
# Thêm hình ảnh từ đường dẫn file
add_picture("path/to/image.jpg", width=4.0)

# Hoặc thêm hình ảnh từ ma trận numpy
import numpy as np
import cv2

img = cv2.imread("path/to/image.jpg")
add_picture(img, width=3.5)
```

### Tạo bảng

```python
# Tạo bảng với 3 hàng và 4 cột
table = add_table(rows=3, cols=4, style="Table Grid")

# Điền dữ liệu vào bảng
table.cell(0, 0).text = "Hàng 1, Cột 1"
table.cell(0, 1).text = "Hàng 1, Cột 2"
# ...
```

## Các màu hỗ trợ

Khi sử dụng các tham số `color` và `highlight`, bạn có thể sử dụng các giá trị sau:

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

## Lưu ý

- Dự án này sử dụng thư viện `python-docx` để tương tác với tài liệu Word
- Các tài nguyên và prompt được lưu trữ trong thư mục `resources` và `prompts`
- Đảm bảo bạn đã cài đặt đầy đủ các thư viện phụ thuộc trước khi chạy server

## Ví dụ hoàn chỉnh

```python
# Tạo tài liệu mới
create_new_document()

# Thêm tiêu đề
add_heading("Báo cáo dự án", level=0)

# Thêm thông tin người tạo
p = add_paragraph("Người tạo: ")
add_run_to_paragraph(p, "Nguyễn Văn A", bold=True)

# Thêm mục lục
add_heading("Mục lục", level=1)
add_paragraph("1. Giới thiệu")
add_paragraph("2. Nội dung")
add_paragraph("3. Kết luận")

# Thêm nội dung
add_heading("1. Giới thiệu", level=1)
add_paragraph("Đây là phần giới thiệu của dự án...")

# Thêm hình ảnh
add_paragraph("Hình ảnh minh họa:")
add_picture("project_diagram.jpg", width=5.0)

# Thêm bảng dữ liệu
add_heading("Bảng dữ liệu", level=2)
table = add_table(rows=3, cols=3)
table.cell(0, 0).text = "Dữ liệu 1"
table.cell(0, 1).text = "Dữ liệu 2"
table.cell(0, 2).text = "Dữ liệu 3"
# Điền các dữ liệu khác...

# Lưu tài liệu
save_document("bao_cao_du_an.docx")
```
