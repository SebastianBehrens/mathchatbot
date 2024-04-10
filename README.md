This repo forms a pipeline to distribute math exercises to students via telegram.
<figure>
    <img width="559" alt="grafik" src="https://github.com/SebastianBehrens/mathchatbot/assets/51058351/c7d9c704-4c44-4dd3-92eb-ebc875bee135">
    <figcaption>Example: Bot `DeinMatheBot` (YourMathBot in german) sending exercises</figcaption>
</figure> 



Exercises are set up in general form. That means every topic contains levels.
Every level is a question or exercise (so called exercise class).
An exercise class refers to the general form of an exercise stored in a level.
Any exercise is formulated in variables only. Those variables are then replaced with specific values, depending on the level. This process is called instantiation.

Any student has a personal config:
```yaml
contact:
  name: Kyle
  telegram_chat_id: '-123'
batch_size: 2
topics:
  fractions:
    max_level: 6
  exponents:
    max_level: 3
past_exercises:
- fractions.level5
- fractions.level4
```
## Set up
1. Create a bot ([Documentation on core.telegram.org](https://core.telegram.org/bots/tutorial#obtain-your-bot-token))
    - Open chat with `@BotFather`.
    - Text him `/newbot`.
    - Enter a name for your bot. (Remember this name will appear as the sender of the exercises.)
2. Store credential on your system, e.g. `.zshrc` and update the reference to it in `send_message_telegram()` by adapting the variable name ([here](https://github.com/SebastianBehrens/mathchatbot/blob/359d070c99c6ce21c0bf0166ec93c98ee9bc1fcc/scripts/send_message_telegram.py#L10)).
3. Create a virtual environment with the supplied requirements.txt (for example: `python -m venv .venv`)
4. Create a group chat to which the bot should talk.
5. Add the bot to the group.
6. Add `@getidsbot` to the group. It determines returns the `chat_id` when added.
7. Create a config in `configs/valid`, and add the `chat_id` to it. Note: Include the minus! It indicates a group chat. You can find a template for a config in `config_template.yaml`.
8. Set up the remaining options in the config.
9. Both bot and config are set up. To test, run: `.venv/bin/python main.py`

## Remarks:
- This program does not contain an internal scheduler. Reason being that this program is intended to be scheduled on a cronjob. Any scheduling between scheduled cronjob execution can still occur through the config.