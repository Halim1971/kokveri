# Kök Veri

Kök Veri Teknolojileri Ltd. Şti. için minimal Flask kurumsal web sitesi.

## Kurulum

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Çalıştırma

```bash
python app.py
```

Yerel adres:

```text
http://127.0.0.1:5058
```

## Render

Render build command:

```bash
pip install -r requirements.txt
```

Render start command:

```bash
gunicorn app:app
```
