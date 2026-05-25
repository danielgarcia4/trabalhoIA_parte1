from src.database.performance_db import (
    cursor
)

def identificar_dificuldades():

    cursor.execute("""
    SELECT topic, AVG(score)
    FROM performance
    GROUP BY topic
    """)

    rows = cursor.fetchall()

    if not rows:

        return "Nenhum dado encontrado."

    dificuldades = []

    for topic, avg_score in rows:

        if avg_score < 6:

            dificuldades.append(
                f"{topic} (média: {avg_score:.1f})"
            )

    if not dificuldades:

        return "Nenhuma dificuldade identificada."

    text = "Dificuldades encontradas:\n\n"

    for d in dificuldades:

        text += f"- {d}\n"

    return text

def recomendar_revisao():

    cursor.execute("""
    SELECT topic, AVG(score)
    FROM performance
    GROUP BY topic
    """)

    rows = cursor.fetchall()

    revisao = []

    for topic, avg_score in rows:

        if avg_score < 6:

            revisao.append(topic)

    if not revisao:

        return "Nenhuma revisão necessária."

    text = "Recomendo revisar:\n\n"

    for topic in revisao:

        text += f"- {topic}\n"

    return text