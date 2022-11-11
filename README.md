# Metis
Metis is a tool for formatting webhooks received from GitHub and forwarding them to Discord.
## Requirements
- Python(3.9 or later)  
- Flask  

You can install the necessary packages by running `pip install -r requirements.txt`.  
## Usage  
First, place the `config.ini` file in the same directory as the `metis.py` file.  
Here's an example of `config.ini`:
```INI
[constants]
discord_webhook_url = ENTER THE DISCORD WEBHOOK URL
flask_port = ENTER THE PORT NUMBER YOU WANT TO USE
```
Now you can run `python3 metis.py` and the server will automatically start accepting webhooks on the specified port.
