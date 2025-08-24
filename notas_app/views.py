from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm

# 🎯 VISTA 1: Muestra todas las notas
def lista_notas(request):
    # 📋 Obtiene todas las notas ordenadas por fecha (más reciente primero)
    notas = Nota.objects.all().order_by('-fecha_creacion')
    # 🎨 Renderiza la plantilla con las notas
    return render(request, 'notas_app/lista_notas.html', {'notas': notas})

# 🎯 VISTA 2: Crea una nueva nota
def nueva_nota(request):
    if request.method == 'POST':  # 📤 Si el formulario se envió
        form = NotaForm(request.POST)
        if form.is_valid():  # ✅ Si los datos son válidos
            form.save()  # 💾 Guarda en la base de datos
            return redirect('lista_notas')  # 🔄 Redirige a la lista
    else:  # 📥 Si es una petición normal (mostrar formulario vacío)
        form = NotaForm()
    # 🎨 Renderiza el formulario
    return render(request, 'notas_app/nueva_nota.html', {'form': form})

# 🎯 VISTA 3: Elimina una nota
def eliminar_nota(request, nota_id):
    # 🔍 Busca la nota o muestra error 404 si no existe
    nota = get_object_or_404(Nota, id=nota_id)
    nota.delete()  # 🗑️ Elimina de la base de datos
    return redirect('lista_notas')  # 🔄 Redirige a la lista