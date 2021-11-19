from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


from django.utils import timezone
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'blog/conteudo.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})


def resumo_experiencia(request ):
    context =  [
        {
            'titulo':'Olá, sou o Gustavo Mesquita Ferreira',
            'subtitulo':'Resumo da Experiência',
            'texto': '''Atualmente estudante do curso superior em análise e desenvolvimento de sistemas, estou no 3° semestre. Estagiário na empresa Nosso Leilão
             atuando tanto na parte de suporte e programação. Perfil analítico, inovador, trabalho bem em grupo, sempre em busca de capacitação e novos 
             conhecimentos.''',
        }
    ]
    return render(request, 'blog/resumo_experiencia.html', {'dados': context})

def experiencia_profissional(request ):
    context =  [
        {            
            'ano':'2021-atualmente',
            'nome': 'Nosso Leilão',
            'texto': ''' 
                Estagiário t.i - Prestar suporte nos equipamentos - Programação no sistema
            ''',
        },
        {            
            'ano':'2021-2021',
            'nome': 'Play Seguros',
            'texto': ''' 
               Estagiário t.i - Auxiliar no processo de configuração de e-mails (IMAP ou POP3). - Instalar e configurar layouts de páginas de websites utilizando WordPress. - Formatar computadores, reinstalar o Windows 10 e instalar o pacote Office. - Prestar suporte remoto via AnyDesk ou TeamViewer aos colaboradores da empresa. 
            ''',
        },
        {          
            'ano':'2019-2019',
            'nome': 'Tatu Bola Jardins',
            'texto': ''' 
                Jovem Aprendiz - Auxilio na parte administrativa. - Recebimento e conferência de mercadorias. - Atendimento telefônico e mídias sócias com clientes. - Lançamento de notas fiscais. - Responsável pela montagem de proposta de eventos.
            ''',
        },
        {
            'ano':'2015-2016',
            'nome': 'WMF Solutions',
            'texto': ''' 
                Jovem Aprendiz - Atendimento telefônico e presencial com clientes. - Controle de arquivos. - Elaboração de planilhas e relatórios gerais. - Suporte a gestão. - Controle de entrada e saída de certificados da norma ISO 9001. - Checagem de databooks. - Atualização dos lotes e números das peças.
            ''',
        }

    ]
    return render(request, 'blog/experiencia_profissional.html', {'dados': context})

def cursos_complementares(request ):
    context =  [
        {            
            'ano':'Dezembro 2019',
            'nome': '',
            'texto': ''' 
                Cerficado Java iniciante ao avançado - udemy Dezembro 2019 
            ''',
        },
        {
            'ano':'Dezembro 2019',
            'nome': '',
            'texto': ''' 
                Scrum básico - udemy- Dezembro 2019
            ''',
        },
        {
            'ano':'Março 2020',
            'nome': '',
            'texto': ''' 
                Cerficicado linguagem C iniciante ao avançado - udemy - Março 2020
            ''',
        },
        {
            'ano':'Março 2020',
            'nome': '',
            'texto': ''' 
                Devops básico - udemy- Março 2020
            ''',
        },
        {
            'ano':'Março 2020',
            'nome': '',
            'texto': ''' 
                Hmtl e css básico ao intermediário - udemy - Março 2020
            ''',
        }
    ]
    return render(request, 'blog/cursos_complementares.html', {'dados': context})

def habilidades_tecnicas(request ):
    context =  [
        {
            'ano':'',
            'nome': 'Desenvolvimento Web',
            'texto': ''' 
                HTML / CSS / Java / Javascript / Python
            ''',
        },
        {
            'ano':'',
            'nome': 'Banco De Dados',
            'texto': ''' 
                MySQL / Oracle
            ''',
        },
        {
            'ano':'',
            'nome': ' Framework',
            'texto': ''' 
               
                Django / Nodejs / React
            ''',
        }
    ]
    return render(request, 'blog/habilidades_tecnicas.html', {'dados': context})

