# Reserva de Quadras Esportivas

API de agendamento de quadras esportivas, construída com Django + Django REST Framework como projeto de estudo.

## Stack
- Python
- Django
- Django REST Framework

## Modelagem
- **Quadra**: `nome`, `tipo`, `preco_hora`
- **Reserva**: `quadra` (FK), `usuario` (FK), `horario_inicio`, `horario_fim`

## Endpoints

| Método | Rota | Ação |
|---|---|---|
| GET | `/agendamentos/quadras/` | Lista quadras |
| POST | `/agendamentos/quadras/` | Cria quadra |

## Como rodar
```bash
python manage.py migrate
python manage.py runserver
```
Acesse `http://127.0.0.1:8000/agendamentos/quadras/`

## Progresso
- [x] Models
- [x] Admin
- [x] Serializers
- [x] CRUD parcial de Quadra (GET, POST)
- [ ] CRUD completo de Quadra (detalhar, atualizar, deletar)
- [ ] CRUD completo de Reserva
- [ ] Validação de conflito de horário
- [ ] Autenticação
- [ ] Testes automatizados