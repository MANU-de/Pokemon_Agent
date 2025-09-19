# How to Register a Pokemon Showdown Account for Authentication

To use authentication tokens in your poke_env agents, you need a registered account on the official Pokemon Showdown server.

## Steps to Register

1. Open your web browser and go to: https://play.pokemonshowdown.com/

2. Click on the "Choose name" button on the top right corner.

3. Enter your desired username and click "OK".

4. If the username is available, you will be logged in as a guest with that name.

5. To register the username, open the chat box and type the following command:

   ```
   /register password email@example.com
   ```

   Replace `password` with your desired password and `email@example.com` with your email address (optional but recommended).

6. You will receive a confirmation message. Follow any additional instructions sent to your email if you provided one.

7. Once registered, you can log in with your username and password.

## Using Your Credentials in Code

Update your agent's `AccountConfiguration` with your username and password:

```python
from poke_env import AccountConfiguration

account_config = AccountConfiguration("username", "password")
```

Use this `account_config` when instantiating your agents to authenticate properly.

---

