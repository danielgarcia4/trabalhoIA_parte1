from src.database.agenda_db import conn, cursor
from src.utils.logger import logger

def adicionar_evento(
    data,
    hora,
    titulo=None,
    descricao=None
):

    # =====================================
    # Compatibilidade com LLM
    # =====================================

    if titulo is None and descricao is not None:

        titulo = descricao

    if titulo is None:

        titulo = "Evento"

    cursor.execute("""
    INSERT INTO agenda (
        titulo,
        data,
        horario
    )
    VALUES (?, ?, ?)
    """, (
        titulo,
        data,
        hora
    ))

    conn.commit()

    logger.info(f"""
    TOOL: adicionar_evento

    TITULO: {titulo}
    DATA: {data}
    HORA: {hora}
    """)

    return "Evento adicionado com sucesso."

def listar_eventos():

    cursor.execute("""
    SELECT * FROM agenda
    """)

    eventos = cursor.fetchall()

    logger.info("""
    TOOL: listar_eventos
    """)

    if not eventos:

        return "Nenhum evento encontrado."

    text = ""

    for evento in eventos:

        text += f"""
ID: {evento[0]}
Título: {evento[1]}
Data: {evento[2]}
Horário: {evento[3]}

"""

    return text