from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_deve_listar_contas_a_pagar_e_receber():
    response = client.get('/contas-a-pagar-e-receber')

    assert response.status_code == 200
    assert response.json() == [
        {'id': 1, 'descricao': 'Aluguel', 'valor': '1000.5', 'tipo': 'PAGAR'}, 
        {'id': 2, 'descricao': 'Salario', 'valor': '5000', 'tipo': 'RECEBER'}
        ]

