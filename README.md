# 🧪 Selenium Automation Framework – SauceDemo

Automation testing framework sử dụng **Python**, **Selenium** và **Pytest** để kiểm thử website [https://www.saucedemo.com](https://www.saucedemo.com).

---

## 📁 Cấu trúc dự án

```
Test/
├── pages/
│   ├── base_page.py          # Các method dùng chung (find_element, click, send_keys, wait...)
│   ├── login_page.py         # Page Object cho trang Login
│   ├── inventory_page.py     # Page Object cho trang Inventory
│   ├── cart_page.py          # Page Object cho trang Cart
│   └── checkout_page.py      # Page Object cho trang Checkout
├── tests/
│   ├── conftest.py           # Setup/Teardown bằng pytest fixtures
│   ├── test_login.py         # Scenario 1: Kiểm thử đăng nhập
│   └── test_checkout.py      # Scenario 2: Thêm sản phẩm & thanh toán
├── utils/
│   └── config_reader.py      # Đọc cấu hình từ testsetting.json
├── assets/
│   └── style.css             # Style cho report HTML
├── pytest.ini                # Cấu hình pytest
├── report.html               # HTML report kết quả test
├── requirements.txt          # Danh sách thư viện
└── testsetting.json          # Cấu hình: base URL, timeout, credentials
```

---

## ⚙️ Yêu cầu cài đặt

- Python >= 3.8
- Google Chrome + ChromeDriver phù hợp với phiên bản Chrome

---

## 🚀 Cài đặt

### 1. Clone dự án

```bash
git clone https://github.com/luxiaofengok/Test.git
cd Test
```

### 2. Tạo môi trường ảo và cài dependencies

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

---

## 🔧 Cấu hình

File `testsetting.json`:

```json
{
  "base_url": "https://www.saucedemo.com/",
  "credentials": {
    "username": "standard_user",
    "password": "secret_sauce"
  },
  "timeout": {
    "implicit_wait": 10,
    "page_load": 30
  }
}
```

File `pytest.ini`:

```ini
[pytest]
pythonpath = .
```

---

## ▶️ Chạy test

### Chạy tất cả test cases

```bash
pytest tests/ -v
```

### Chạy từng scenario

```bash
# Scenario 1 – Login
pytest tests/test_login.py -v

# Scenario 2 – Add to cart & Checkout
pytest tests/test_checkout.py -v
```

### Chạy và xuất HTML report

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

---

## 📋 Mô tả các Test Scenario

### ✅ Scenario 1 – Đăng nhập thành công 

| Bước | Mô tả |
|------|-------|
| 1 | Truy cập `https://www.saucedemo.com/` |
| 2 | Nhập username: `standard_user`, password: `secret_sauce` |
| 3 | Click nút **Login** |
| 4 | Xác nhận được chuyển hướng đến trang Inventory (kiểm tra URL hoặc tiêu đề trang) |

---

### ✅ Scenario 2 – Thêm 3 sản phẩm và thanh toán 

| Bước | Mô tả |
|------|-------|
| 1 | Sau khi đăng nhập, chọn bất kỳ 3 sản phẩm và thêm vào giỏ hàng |
| 2 | Click icon giỏ hàng → Click **Checkout** |
| 3 | Nhập: First Name: `John`, Last Name: `Doe`, Zip: `70000` |
| 4 | Click **Continue** → Click **Finish** |
| 5 | Xác nhận thông báo: *"Thank you for your order!"* |

---

## 🏗️ Kiến trúc – Page Object Model (POM)

Framework áp dụng mô hình **Page Object Model**, tách biệt logic test và logic thao tác giao diện:

- **`base_page.py`** – Chứa các method tái sử dụng: `find_element()`, `click()`, `send_keys()`, `wait_for_element()` sử dụng `WebDriverWait`.
- **`pages/`** – Mỗi file tương ứng một màn hình trên ứng dụng.
- **`tests/conftest.py`** – Khởi tạo và đóng WebDriver qua pytest fixtures (scope: function/session).
- **`utils/config_reader.py`** – Đọc cấu hình từ `testsetting.json`.

---

## 👤 Tác giả

- **Họ tên:** Cuong Pham
- **GitHub:** [luxiaofengok](https://github.com/luxiaofengok)
- **Khóa học:** Selenium Automation with Python