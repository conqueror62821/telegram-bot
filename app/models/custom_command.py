class CustomCommand:
    @staticmethod
    def help_command():
        return 'k andai pidiendo ayuda ctm'
    
    @staticmethod
    def creator_command():
        return 'Mi creador :3'
    
    @staticmethod
    def about_command():
        return 'Soy un arma de destruccion masiva :3'
    
    @staticmethod
    async def onichan_command(bot, chat_id: str):
        from settings.media import MEDIA_URLS
        import random
        element = random.choice(MEDIA_URLS)
        await bot.send_photo(chat_id=chat_id, photo=element)

