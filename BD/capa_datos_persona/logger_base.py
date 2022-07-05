import logging as log

# asctime agrega fecha y hora
# levelname indica si fue DEBUB, INFO, WARNING, ERROR O CRITICAL
# agrega el nombre del archivo al mensaje del log
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

# HANDLER es un recurso a donde vamos a mandar esta información

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel de critico')
