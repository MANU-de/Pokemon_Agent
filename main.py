import asyncio
from poke_env import RandomPlayer, AccountConfiguration as PlayerConfiguration, ServerConfiguration, LocalhostServerConfiguration, ShowdownServerConfiguration
from TemplateAgent import TemplateAgent  # Import your agent

async def main():
    # Instantiate your agent with PlayerConfiguration and ServerConfiguration
    my_agent = TemplateAgent(
        account_configuration=PlayerConfiguration("username", "password"),
        server_configuration=LocalhostServerConfiguration,
        battle_format="randombattle",
    )

    # Instantiate an opponent agent (RandomPlayer)
    opponent = RandomPlayer()

    # Let the agent battle the opponent
    print("Starting battle between YourAgent and RandomPlayer...")
    await my_agent.battle_against(opponent, n_battles=1)
    print(f"Battle finished. Your agent won {my_agent.n_won_battles} / {my_agent.n_battles} battles.")

    # Cross-evaluate the agent against multiple random players
    print("\nCross-evaluating your agent against multiple random players...")
    await my_agent.train_against(
        opponent=RandomPlayer(
            account_configuration=PlayerConfiguration("PlaceholderOpponent2", "placeholderpassword2"),
            server_configuration=LocalhostServerConfiguration,
            battle_format="randombattle",
        ),
        n_battles=5
    )
    print(f"Cross-evaluation finished. Your agent won {my_agent.n_won_battles} / {my_agent.n_battles} battles.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())