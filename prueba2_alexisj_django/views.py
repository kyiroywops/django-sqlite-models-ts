from django.shortcuts import render, redirect
import sqlite3



def main(request):
    
    return render(request, 'index.html')

## Compare this snippet from prueba2_alexisj_django/wsgi.py:
def verProductos(request):
    con = sqlite3.connect('prueba2_django.db')
    c = con.cursor()
    product = c.execute("SELECT * FROM producto")
    
    return render(request, 'verProductos.html', {'productos': product})

# Compare this snippet from prueba2_alexisj_django/urls.py:
def frmVenta(request, id):
    con = sqlite3.connect('prueba2_django.db')
    c = con.cursor()
    product = c.execute("SELECT * FROM producto WHERE codigo = ?", [id])
    UniqueProduct = product.fetchall()
    if request.method == 'POST':
        cantidad = request.POST['cantidad']
        sql = "UPDATE producto SET stock = stock - ? WHERE codigo = ?"
        datos = [cantidad, id]
        c.execute(sql, datos)
        con.commit()
        con.close()
        return redirect('verProductos')
    return render(request, 'frmVenta.html', {'producto': UniqueProduct})

# Compare this snippet from prueba2_alexisj_django/wsgi.py:
def venta(request):
    con = sqlite3.connect('prueba2_django.db')
    c = con.cursor()
    product = c.execute("SELECT * FROM producto")
    
    return render(request, 'venta.html', {'productos': product})

