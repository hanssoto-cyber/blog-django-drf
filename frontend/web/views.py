import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AuthorCreateForm, ArticleCreateForm

API_BASE = "http://127.0.0.1:8000/api/v1"


def _api_error(resp):
    try:
        data = resp.json()
    except Exception:
        return resp.text
    if isinstance(data, dict):
        parts = []
        for k, v in data.items():
            parts.append(f"{k}: {'; '.join(map(str, v)) if isinstance(v, list) else v}")
        return " | ".join(parts)
    if isinstance(data, list):
        return "; ".join(map(str, data))
    return str(data)


def articles_list(request):
    articles = []
    error = None
    try:
        r = requests.get(f"{API_BASE}/articles/", timeout=10)
        r.raise_for_status()
        articles = r.json()
    except Exception as e:
        error = f"No se pudo cargar artículos: {e}"
    return render(request, "web/articles_list.html", {"articles": articles, "error": error})


def authors_list(request):
    authors = []
    error = None
    try:
        r = requests.get(f"{API_BASE}/authors/", timeout=10)
        r.raise_for_status()
        authors = r.json()
    except Exception as e:
        error = f"No se pudo cargar autores: {e}"
    return render(request, "web/authors_list.html", {"authors": authors, "error": error})


def author_create(request):
    if request.method == "POST":
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            payload = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "bio": form.cleaned_data.get("bio", ""),
            }
            bd = form.cleaned_data.get("birth_date")
            if bd:
                payload["birth_date"] = bd.isoformat()
            try:
                r = requests.post(f"{API_BASE}/authors/", json=payload, timeout=10)
                if r.status_code >= 400:
                    messages.error(request, f"Error al crear autor: {_api_error(r)}")
                else:
                    messages.success(request, "Autor creado correctamente.")
                    return redirect("authors_list")
            except Exception as e:
                messages.error(request, f"Error conectando con la API: {e}")
    else:
        form = AuthorCreateForm()
    return render(request, "web/author_create.html", {"form": form})


def article_create(request):
    authors_choices = []
    try:
        ar = requests.get(f"{API_BASE}/authors/", timeout=10)
        ar.raise_for_status()
        authors_choices = [(str(a["id"]), a["name"]) for a in ar.json()]
    except Exception:
        authors_choices = []

    if request.method == "POST":
        form = ArticleCreateForm(request.POST)
        form.fields["author_id"].choices = authors_choices
        if form.is_valid():
            payload = {
                "title": form.cleaned_data["title"],
                "content": form.cleaned_data["content"],
                "author_id": int(form.cleaned_data["author_id"]),
                "status": form.cleaned_data["status"],
            }
            pa = form.cleaned_data.get("published_at")
            if pa:
                payload["published_at"] = pa.isoformat()
            try:
                r = requests.post(f"{API_BASE}/articles/", json=payload, timeout=10)
                if r.status_code >= 400:
                    messages.error(request, f"Error al crear artículo: {_api_error(r)}")
                else:
                    messages.success(request, "Artículo creado correctamente.")
                    return redirect("articles_list")
            except Exception as e:
                messages.error(request, f"Error conectando con la API: {e}")
    else:
        form = ArticleCreateForm()
        form.fields["author_id"].choices = authors_choices
        if not authors_choices:
            messages.warning(request, "No hay autores disponibles. Crea uno primero.")
    return render(request, "web/article_create.html", {"form": form})