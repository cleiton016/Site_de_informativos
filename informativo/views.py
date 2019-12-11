from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator, InvalidPage
from django.utils.timezone import localdate
from .models import Informativos
from django.views.defaults import bad_request, server_error
from .forms import InsereForm, PesqForm, InforForm
ITEMS_PER_PAGE = 10
# Create your views here.
def red(request):
    return redirect('home')
def home(request):
    form = PesqForm(request.POST or None)
    if request.method == 'POST':
        texto_da_pesquisa = request.POST.get('busca')
        if texto_da_pesquisa is not None:
            dados = Informativos.objects.filter(info__icontains=texto_da_pesquisa)
            form = PesqForm()
    else:
        dados = Informativos.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(dados, ITEMS_PER_PAGE)
    total = paginator.count
    try:
        events = paginator.page(page)
    except InvalidPage:
        events = paginator.page(1)
    return render(request, 'informativo/index.html', {'informativos':dados, "today": localdate(), "total": total, "events": events, 'form':form})

def pdf_view(request, key):
    doc = Informativos.objects.get(pk=int(key))
    nome = doc.arquivo.name.split('/')[1]
    with open('media/'+doc.arquivo.name, 'rb') as pdf: #errors='ignore', encoding="UTF-8"
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename='+nome
        return response
    pdf.closed

def inserir(request):
    if request.method=='POST':
        form = InforForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #dados = Informativos(nome=request.POST['nome'], info=request.POST['info'], arquivo=form.arq)
            #dados.save()
            return redirect('home')#render(request, 'informativo/sucesso.html',{'valido':True,'dados':form['arq']})
    else:
        form = InforForm()
    return render(request, 'informativo/inserir.html',{'form':form})