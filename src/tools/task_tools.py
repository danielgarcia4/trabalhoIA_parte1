from src.database.tasks_db import conn, cursor
from src.utils.logger import logger

def adicionar_tarefa(tarefa):

    cursor.execute("""
    INSERT INTO tasks (tarefa)
    VALUES (?)
    """, (tarefa,))

    conn.commit()

    logger.info(f"""
    TOOL: adicionar_tarefa
    INPUT: {tarefa}
    """)

    return "Tarefa adicionada."

def listar_tarefas():

    cursor.execute("""
    SELECT * FROM tasks
    """)

    tarefas = cursor.fetchall()

    logger.info("""
    TOOL: listar_tarefas
    """)

    if not tarefas:

        return "Nenhuma tarefa encontrada."

    text = ""

    for tarefa in tarefas:

        status = (
            "Concluída"
            if tarefa[2] == 1
            else "Pendente"
        )

        text += f"""
ID: {tarefa[0]}
Tarefa: {tarefa[1]}
Status: {status}

"""

    return text

def concluir_tarefa(task_id):

    cursor.execute("""
    UPDATE tasks
    SET concluida = 1
    WHERE id = ?
    """, (task_id,))

    conn.commit()

    logger.info(f"""
    TOOL: concluir_tarefa
    INPUT: {task_id}
    """)

    return "Tarefa concluída."