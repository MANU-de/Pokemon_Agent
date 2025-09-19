from poke_env import RandomPlayer, cross_evaluate, AccountConfiguration as PlayerConfiguration, ServerConfiguration, LocalhostServerConfiguration, ShowdownServerConfiguration
from poke_env.battle.battle import Battle
from poke_env.battle.move import Move
from poke_env.battle.pokemon import Pokemon
from LLMAgentBase import LLMAgentBase  # Import our base class

class TemplateAgent(LLMAgentBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.battle_history = []  # To store battle logs or key decisions

    def choose_move(self, battle: Battle):
        # This is where the custom agent logic will go!
        # For now, let's make a slightly smarter random choice:
        # Prioritize damaging moves if available, otherwise switch, otherwise random.

        # Log the current state (optional, for debugging/analysis)
        self.battle_history.append(self._battle_to_prompt(battle))

        # Example: Try to use a damaging move
        damaging_moves = [
            move for move in battle.available_moves 
            if move.category is not None and move.category.name != "STATUS"
        ]
        if damaging_moves:
            return self.create_order(self.choose_random_move(battle, damaging_moves))
        
        # If no damaging moves, try to switch if current pokemon is low HP
        if battle.active_pokemon.current_hp / battle.active_pokemon.max_hp < 0.3 and battle.available_switches:
            # Switch to a random available pokemon
            return self.create_order(self.choose_random_move(battle, battle.available_switches))

        # Fallback to default LLMAgentBase's random choice (or more advanced LLM call)
        return super().choose_move(battle)

    def choose_random_move(self, battle: Battle, options=None):
        if options is None:
            options = battle.available_moves + battle.available_switches
        
        if options:
            import random
            return random.choice(options)
        return self.create_order(None)  # No available moves or switches

player_config = PlayerConfiguration("username", "password")
server_config = LocalhostServerConfiguration

my_agent = TemplateAgent(
    account_configuration=player_config,
    server_configuration=server_config,
    battle_format="randombattle",  # Specify the battle format
)
