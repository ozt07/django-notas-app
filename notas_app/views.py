from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Calculo
from .forms import CalculadoraForm
import math

@login_required
def calculadora(request):
    historial = Calculo.objects.filter(usuario=request.user).order_by('-fecha_creacion')[:10]
    
    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            expresion = form.cleaned_data['expresion']
            try:
                # Evaluar la expresión de forma segura
                resultado = eval(expresion, {"__builtins__": None}, {
                    'sqrt': math.sqrt,
                    'sin': math.sin,
                    'cos': math.cos,
                    'tan': math.tan,
                    'log': math.log,
                    'pi': math.pi,
                    'e': math.e
                })
                
                # Guardar en el historial
                Calculo.objects.create(
                    usuario=request.user,
                    expresion=expresion,
                    resultado=resultado
                )
                
                return render(request, 'notas_app/calculadora.html', {
                    'form': form,
                    'resultado': resultado,
                    'expresion': expresion,
                    'historial': historial
                })
                
            except Exception as e:
                error = f"Error en la expresión: {str(e)}"
                return render(request, 'notas_app/calculadora.html', {
                    'form': form,
                    'error': error,
                    'historial': historial
                })
    else:
        form = CalculadoraForm()
    
    return render(request, 'notas_app/calculadora.html', {
        'form': form,
        'historial': historial
    })

@login_required
def borrar_historial(request):
    if request.method == 'POST':
        Calculo.objects.filter(usuario=request.user).delete()
    return redirect('notas_app:calculadora')