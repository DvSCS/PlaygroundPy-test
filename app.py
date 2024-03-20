from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para armazenar os resultados dos códigos executados
resultados = []

def executar_codigo_python(codigo):
    try:
        # Executa o código Python
        resultado = eval(codigo)
        return resultado
    except Exception as e:
        return f"Erro ao executar o código: {str(e)}"

@app.route('/execute', methods=['POST'])
def execute_code():
    # Obtém o código Python enviado pelo cliente
    codigo = request.json.get('code')

    # Executa o código Python
    resultado = executar_codigo_python(codigo)

    # Armazena o resultado e retorna a URL com o ID do resultado
    resultados.append(resultado)
    result_id = len(resultados) - 1
    return jsonify({'result_id': result_id})

if __name__ == '__main__':
    app.run(debug=True)