import logging
import logging.config
from pathlib import Path

# Caminho do arquivo de configuração
LOGGING_CONFIG_PATH = Path(__file__).parent / "logging_config.ini"

# Configuração do Logger
def setup_logger():
    """
    Configura o logger usando o arquivo .ini e retorna a instância do logger.
    """
    try:
        logging.config.fileConfig(LOGGING_CONFIG_PATH, disable_existing_loggers=False)
        return logging.getLogger("root")
    except Exception as e:
        print(f"Erro ao configurar o logger: {e}")
        raise

# Instância do logger
logger = setup_logger()