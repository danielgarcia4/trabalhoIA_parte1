import json

from src.llm.client import ask_llm
from src.agent.prompts import SYSTEM_PROMPT

from src.tools.rag_tools import buscar_material_rag

from src.tools.task_tools import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa
)

from src.tools.agenda_tools import (
    adicionar_evento,
    listar_eventos
)

from src.tools.learning_tools import (
    gerar_exercicios
)

TOOLS = {

    "buscar_material_rag": buscar_material_rag,

    "listar_tarefas": listar_tarefas,

    "adicionar_tarefa": adicionar_tarefa,

    "concluir_tarefa": concluir_tarefa,

    "listar_eventos": listar_eventos,

    "adicionar_evento": adicionar_evento,

    "gerar_exercicios": gerar_exercicios
}

def clean_json_response(response):

    response = response.strip()

    response = response.replace(
        "```json",
        ""
    )

    response = response.replace(
        "```",
        ""
    )

    return response.strip()

def run_agent(user_input):

    prompt = f"""
    {SYSTEM_PROMPT}

    Usuário:
    {user_input}
    """

    response = ask_llm(prompt)

    print("\n========================")
    print("RESPOSTA BRUTA DA LLM:")
    print("========================")
    print(response)

    response = clean_json_response(response)

    print("\n========================")
    print("JSON LIMPO:")
    print("========================")
    print(response)

    try:

        action = json.loads(response)

    except Exception as e:

        return f"""
Erro ao interpretar resposta da LLM.

Resposta recebida:
{response}

Erro:
{str(e)}
"""

    tool_name = action.get("tool")

    tool_input = action.get("input")

    if tool_name not in TOOLS:

        return f"""
Ferramenta inválida:
{tool_name}
"""

    try:

        # múltiplos parâmetros
        if isinstance(tool_input, dict):

            result = TOOLS[tool_name](
                **tool_input
            )

        # parâmetro único
        else:

            result = TOOLS[tool_name](
                tool_input
            )

        return result

    except Exception as e:

        return f"""
Erro ao executar ferramenta.

Ferramenta:
{tool_name}

Erro:
{str(e)}
"""