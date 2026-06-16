from django import forms


class AuthorCreateForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        label='Nombre completo',
        widget=forms.TextInput(attrs={'placeholder': 'Ej: Ana González'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'ana@blog.com'})
    )
    bio = forms.CharField(
        label='Biografía',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Breve descripción del autor...'})
    )
    birth_date = forms.DateField(
        label='Fecha de nacimiento',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )


class ArticleCreateForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Título',
        widget=forms.TextInput(attrs={'placeholder': 'Título del artículo'})
    )
    content = forms.CharField(
        label='Contenido',
        widget=forms.Textarea(attrs={'rows': 6, 'placeholder': 'Escribe el contenido...'})
    )
    author_id = forms.ChoiceField(label='Autor')
    status = forms.ChoiceField(
        label='Estado',
        choices=[('draft', 'Borrador'), ('published', 'Publicado')],
    )
    published_at = forms.DateTimeField(
        label='Fecha de publicación',
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )