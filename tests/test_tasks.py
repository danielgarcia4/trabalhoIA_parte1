from src.tools.task_tools import adicionar_tarefa

def test_add_task():

    response = adicionar_tarefa(
        "Estudar embeddings"
    )

    assert response == "Tarefa adicionada."