import asyncio
from poke_env import RandomPlayer, AccountConfiguration as PlayerConfiguration, ServerConfiguration, LocalhostServerConfiguration, ShowdownServerConfiguration
from TemplateAgent import TemplateAgent

async def test_instantiation():
    try:
        # Test agent instantiation
        my_agent = TemplateAgent(
            account_configuration=PlayerConfiguration("username", None),
            server_configuration=LocalhostServerConfiguration,
            battle_format="randombattle",
        )
        print("✓ TemplateAgent instantiated successfully")

        # Test opponent instantiation
        opponent = RandomPlayer(
            account_configuration=PlayerConfiguration.generate("PlaceholderOpponent", "placeholderpassword"),
            server_configuration=ShowdownServerConfiguration,
            battle_format="randombattle",
        )
        print("✓ RandomPlayer instantiated successfully")

        print("All instantiations passed critical-path testing.")
        return True
    except Exception as e:
        print(f"✗ Instantiation failed: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.get_event_loop().run_until_complete(test_instantiation())
    if success:
        print("Critical-path testing for instantiation: PASSED")
    else:
        print("Critical-path testing for instantiation: FAILED")
