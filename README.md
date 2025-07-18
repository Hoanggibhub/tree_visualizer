# 📦 Tree Visualizer

**Tree Visualizer** là thư viện Python mạnh mẽ giúp trực quan hóa và phân tích cấu trúc dữ liệu dạng cây (đặc biệt là JSON, Dict lồng nhau, XML,...).

---

## 🚀 Các tính năng nổi bật

### 🎯 Trực quan hóa dữ liệu cây

- Hiển thị rõ ràng cấu trúc phân cấp của dữ liệu như:
  - JSON trả về từ API
  - File cấu hình
  - AST (Abstract Syntax Tree)
  - DOM, XML
- Dễ dàng nhận biết node lồng sâu, key trùng, cấu trúc lỗi.

✅ Giúp tiết kiệm thời gian debug và hiểu luồng dữ liệu.

---

### 🔍 Highlight theo Path

- Cho phép highlight một hoặc nhiều đường dẫn như `"user/preferences/notifications"`
- Dễ dàng theo dõi key/value quan trọng trong cây.

---

### 🧭 Tương tác Web UI

- Zoom / Pan / Mini-map
- Collapse / Expand từng node
- Hover để xem giá trị nhanh chóng

---

### 📊 Phân tích và Kết xuất

- Hỗ trợ xuất:
  - Ảnh PNG / SVG / PDF với Graphviz
  - Ảnh động GIF (hiệu ứng xây dựng cây)
  - Web interactive HTML viewer
  - File CSV / JSON cho phân tích

---

## 🌐 Ứng dụng thực tế

| Tình huống sử dụng | Lợi ích |
|--------------------|--------|
| Debug dữ liệu JSON phức tạp | Dễ dàng xác định lỗi |
| Trình xem cấu trúc dữ liệu game / config | Hiển thị trực quan, dễ thao tác |
| Công cụ frontend kiểm tra API | Highlight rõ từng node |
| Viewer nội bộ cho team backend / AI | Tối ưu hiểu dữ liệu trung gian |
| Plugin IDE (VSCode, Jupyter) | Hiển thị cây ngay trong trình soạn thảo |

---

## 🧪 Demo nhanh

```python
from tree_visualizer import TreeVisualizer

tree = {"user": {"profile": {"name": "Alice"}, "settings": {"theme": "dark"}}}
tv = TreeVisualizer(tree)
tv.to_graphviz("output", format="png")      # Xuất ảnh PNG
tv.to_html("output.html")                   # Web interactive
```

---

## 🌍 Góp ý & Đóng góp

Pull request và issue luôn được hoan nghênh. Hãy giúp cải thiện công cụ này cho cộng đồng Python!

## 📦 Cài đặt

### Cài đặt từ mã nguồn

```bash
git clone https://github.com/Hoanggibhub/tree_visualizer.git
cd tree_visualizer
pip install -e .
```

### Yêu cầu

- Python 3.7+
- Các thư viện:
  - `graphviz`
  - `jinja2`
  - `setuptools` (nếu cài editable mode)
  - Cài đặt thêm graphviz (hệ điều hành):
    - Ubuntu: `sudo apt install graphviz`
    - Windows: [Tải Graphviz](https://graphviz.org/download/)

## 🚀 Sử dụng nhanh

```python
from tree_visualizer import TreeAnalyzer, GraphvizExporter

tree = {"a": {"b": 1, "c": [2, 3]}}

analyzer = TreeAnalyzer(tree)
exporter = GraphvizExporter()
exporter.export(tree, "output", format="png")
```

Kết quả sẽ được lưu ở file `output.png`.
