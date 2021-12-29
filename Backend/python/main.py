import re
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
#Esta linea permite a la api hacer peticiones externas o desde otrso programas
cors = CORS(app, resources={r"/*": {"origin": "*"}})

cancionesMasReproducidas = []
topArtistas = []
@app.route("/CancionesEscuchadas", methods=['POST'])
def recibirDatosCanciones():
    global cancionesMasReproducidas
    cancionesMasReproducidas = []
    canciones = request.json
    for i in canciones:
        # print(i["nombreCancion"], i["reproducciones"])
        listaAux = []
        listaAux.append(i["nombreCancion"])
        listaAux.append(i["reproducciones"])
        cancionesMasReproducidas.append(listaAux[:])
    
    #ordenamiento burbuja
    for i in range (len(cancionesMasReproducidas)-1):      
        for j in range(len(cancionesMasReproducidas)-1):
            if cancionesMasReproducidas[j][1]<cancionesMasReproducidas[j+1][1]:
                tmp = cancionesMasReproducidas[j]
                cancionesMasReproducidas[j] = cancionesMasReproducidas[j+1]
                cancionesMasReproducidas[j+1] = tmp
    # for i in cancionesMasReproducidas:
    #     print(i[1], 'ooo')
    # print(cancionesMasReproducidas[0][1], cancionesMasReproducidas[0][0])
    # print(cancionesMasReproducidas[1][1], cancionesMasReproducidas[1][0])
    # print(cancionesMasReproducidas[2][1], cancionesMasReproducidas[2][0])

    # print(canciones)
    respuesta = []
    for i in range(5):
        respuesta.append({"nombreCancion": cancionesMasReproducidas[i][0], "reproducciones": cancionesMasReproducidas[i][1]})
        
    return jsonify(respuesta)
@app.route("/ArtistasEscuchados", methods=['POST'])
def artistasMasEscuchados():
    global topArtistas
    topArtistas = []
    artistas = request.json
    print(artistas)
    for i in artistas:
        listaAuxArtistas = []
        listaAuxArtistas.append(i["nombreArtista"])
        listaAuxArtistas.append(i["reproducciones"])
        topArtistas.append(listaAuxArtistas[:])
    for i in range (len(topArtistas)-1):      
        for j in range(len(topArtistas)-1):
            if topArtistas[j][1]<topArtistas[j+1][1]:
                tmp = topArtistas[j]
                topArtistas[j] = topArtistas[j+1]
                topArtistas[j+1] = tmp
    respuesta = []
    for i in range(3):
        respuesta.append({"nombreArtista": topArtistas[i][0], "reproducciones": topArtistas[i][1]})

    return jsonify(respuesta)
if __name__ == "__main__":
    app.run(debug=True, port=5000)

