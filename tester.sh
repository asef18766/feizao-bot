if [ ! -f .env ]; then
    heroku config:get DATABASE_URL -s -a feizao-bot >> .env
    heroku config:get DATA_CENTER_URL -s -a feizao-bot >> .env
    heroku config:get LINE_BOT_API -s -a feizao-bot  >> .env
    heroku config:get WEBHOOK_HANDLER -s -a feizao-bot >> .env
    heroku config:get IMGUR_ID -s -a feizao-bot >> .env
    heroku config:get IMGUR_SECRET -s -a feizao-bot >> .env
    heroku config:get IMGUR_ACCESS_TOKEN -s -a feizao-bot >> .env
    heroku config:get IMGUR_REFRESH_TOKEN -s -a feizao-bot >> .env
    heroku config:get HISUKURIFU -s -a feizao-bot >> .env
fi
heroku local -e .env