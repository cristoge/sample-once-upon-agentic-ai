# TODO: Step 1 - Add debug logging to see what your agent is thinking
import logging

from strands import Agent

# Configure the root strands logger
logging.getLogger("strands").setLevel(logging.DEBUG)

# Add a handler to see the logs
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", handlers=[logging.StreamHandler()]
)
# TODO: Step 2 - Create the agent with the following system prompt: "You are a game master for a fantasy role-playing game"
agent = Agent(
    system_prompt=(
        "Eres el master de un juego de rol de fantasia"
        "Puedes crear personajes, historias y situaciones para el juego"
        "Puedes interactuar con los jugadores y hacer que se diviertan"
        "Puedes interactuar con los jugadores y responder a sus preguntas"
        "Puedes crear un mundo de fantasia y hacer que los jugadores se sumerjan en el"
    )
)
# TODO: Step 3 - Invoke your agent with a basic query such as "Hi, I am an adventurer ready for adventure!"
agent("Creame 2 jugadores")
