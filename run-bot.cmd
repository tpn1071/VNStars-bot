@echo off
REM Navigate to the project directory
cd /d "d:\Project\DiscordBot\VNStars-bot"

REM Activate the virtual environment if applicable
REM call venv\Scripts\activate

REM Run the bot
python -m bot.main

pause