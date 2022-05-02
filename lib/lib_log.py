import logging as _log

class Log:
    def __init__(self, target: str = 'main') -> None:
        self.logger = _log
        self.logger.basicConfig(format='[%(levelname)s] In %(name)s - %(asctime)s - %(message)s',
                                datefmt='%d-%b-%y %H:%M:%S',
                                level=self.logger.INFO,
                                handlers=[
                                    self.logger.FileHandler('log/log.log', mode='a', encoding='utf-8'),
                                    self.logger.StreamHandler()
                                ]
                                )
        self.target = '[' + target.upper() + '] '

    def debug(self, msg, *args, **kwargs) -> None:
        self.logger.debug(self.target + msg, *args, **kwargs)
        return

    def info(self, msg, *args, **kwargs) -> None:
        self.logger.info(self.target + msg, *args, **kwargs)
        return

    def warn(self, msg, *args, **kwargs) -> None:
        self.logger.warning(self.target + msg, *args, **kwargs)
        return

    def error(self, msg, *args, **kwargs) -> None:
        self.logger.error(self.target + msg, *args, **kwargs)
        return

    def critical(self, msg, *args, **kwargs) -> None:
        self.logger.critical(self.target + msg, *args, **kwargs)
        return

    def exception(self, msg, *args, **kwargs) -> None:
        self.logger.exception(self.target + msg, *args, **kwargs)
        return
