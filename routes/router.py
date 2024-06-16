from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.atencionDaoControl import AtencionDaoControl
router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito

@router.route('/')
def home():
    return render_template('template.html')


#---------------------ATENCIONES----------------------

@router.route('/atenciones')
def ver_atenciones():
    at = AtencionDaoControl()
    list = at._list()
    #list.sort_models("_nombre", 1, "Quick")
    return render_template('nene/lista_p.html', lista=at.to_dict_lista(list))

@router.route('/atenciones/<tipo>/<attr>/<metodo>')
def ver_atenciones_ordenar(tipo, attr, metodo):
    at = AtencionDaoControl()
    list = at._list()
    list.sort_models(attr, int(tipo), str(metodo))
    return render_template('nene/lista_p.html', lista=at.to_dict_lista(list))

@router.route('/atencionesBuscar/<data>/<attr>/<metodo>')
def ver_atenciones_buscar(data, attr, metodo):
    at = AtencionDaoControl()
    list = at._list()
    list.sort_models(attr, 1, "Quick")
    listaAux =  list.busqueda_binaria_o_secuencial_binaria_models(data, attr, metodo)
    if listaAux == None:
        return render_template('nene/notFound.html')
    else:
        return render_template('nene/lista_p.html', lista=at.to_dict_lista(listaAux))

@router.route('/atenciones/formulario')
def ver_guardar_atencion():
    return render_template('nene/guardar_p.html')

@router.route('/atenciones/guardar', methods=['POST'])
def guardar_atencion():
    at = AtencionDaoControl()
    data = request.form
    
    at._atencion._nombre = data['nombre']
    at._atencion._tiempoDeAtencion = data['tiempoDeAtencion']
    at._atencion._calificacion = data['calificacion']
    at._atencion._fechaDeAtencion = data['fechaDeAtencion']
    at.save
    return redirect('/atenciones', code=302)


@router.route('/atenciones/eliminar', methods =['POST'])
def eliminar_atencion():
    at = AtencionDaoControl()
    pos = request.form["id"]
    at.delete(int(pos)-1)
    return redirect("/atenciones",code=302)

@router.route('/atenciones/editar/<pos>')
def ver_editar_atencion(pos):
    at = AtencionDaoControl()
    nene = at._get(int(pos))#at._list().get(int(pos) -1)
    return render_template("nene/editar_p.html", data = nene )

@router.route('/atenciones/modificar', methods=['POST'])
def modificar_atencion():
    at = AtencionDaoControl()
    data = request.form
    pos = int(data['id'])-1
    nene = at._list().get(pos)
    
    at._atencion = nene
    at._atencion._nombre = data['nombre']
    at._atencion._tiempoDeAtencion = data['tiempoDeAtencion']
    at._atencion._calificacion = data['calificacion']
    at._atencion._fechaDeAtencion = data['fechaDeAtencion']
    at.merge(pos)
    return redirect('/atenciones', code=302)