import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6020884861:AAEq-BUAOM66etvIFFCCTcvdNowNTpVCvzk)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOI0Bu23Tnht4Anu1KPaYwnAC8NMm2LJx68FFSDNYM4f0J5uj4DvXZRBX4S0uRvFPWx-ceSYnzOIRTLpBWBWSOOCUx2coHSgcH9DtsSoILeKFH3xV2uaUgYDXwx-hy4yrp8GCz6PTxqQ1VYhQ0JFr1s8yVSYKo4aG3xi8fBz9_8uFI67ng5JTyY52YVg7QZihHSDkPIGGOtB3RM1fkIYgx9I3Ogn8j5VqszCa2o8NvU8UWHtwG0quKWQkFO-gHn5PisCRmTKXAPOygvq8vC2C60vpM95S6m7STLOO4SIwMBJhVjdrADTebyJiXiMrac_OwCKE78lwqV20d4uMFQ2XV8qlDgA=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
