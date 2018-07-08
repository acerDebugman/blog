import os
import sys
import logging
import datetime
from config import *
from mmh3 import hash64
from sendmail import send
from rediscluster import StrictRedisCluster


def init_logger(version, step):
    if not os.path.isdir('logs'): os.mkdir('logs') 
    log_file = 'logs/{version}.{step}.log'.format(version=version, step=step)
    logging.basicConfig(format='%(asctime)s %(message)s', filename=log_file, level=logging.INFO)
    

def get_pipeline():
    startup_nodes = [{"host": REDIS_HOST, "port": REDIS_PORT}]
    connection = StrictRedisCluster(startup_nodes=startup_nodes)
    return connection.pipeline()


def process_file(tenant, file_path, pipeline, lines):
    line_counter = lines
    with open(file_path) as f:
        for line in f:
            uuid, tids = line.strip().split(LINE_DELIMITER)
            hashed_bytes = hash64(uuid)[0].to_bytes(HASH_BYTES, byteorder=BYTE_ORDER, signed=HASH_SIGNED)
            tenant_bytes = int(tenant).to_bytes(1, byteorder=BYTE_ORDER, signed=HASH_SIGNED)
            redis_key, redis_field = tenant_bytes + hashed_bytes[:KEY_BYTES], hashed_bytes[KEY_BYTES:KEY_BYTES + FIELD_BYTES]
            
            redis_value = bytearray()
            for tid in tids.split(TID_DELIMITER):
                 redis_value.extend(int(tid).to_bytes(TID_BYTES, byteorder=BYTE_ORDER, signed=HASH_SIGNED))
            pipeline.hset(redis_key, redis_field, bytes(redis_value))

            line_counter += 1
            if line_counter % PIPELINE_SIZE == 0:
                pipeline.execute()
                logging.info(line_counter)

    pipeline.execute()
    return line_counter


def run():
    if len(sys.argv) < 4:
        print('Usage: python set.py tenant version add|change path ...')
        exit(1)

    tenant = sys.argv[1]
    version = sys.argv[2]
    step = sys.argv[3]
    file_paths = sys.argv[4:]

    init_logger(version, step)
    logging.info(version)
    logging.info(file_paths)

    lines = 0
    is_panel = False
    pipeline = get_pipeline()
    for file_path in file_paths:
        logging.info(file_path)
        lines = process_file(tenant, file_path, pipeline, lines)
        if 'panel' in file_path:
           is_panel = True

    logging.info('DONE: {}'.format(lines))
    if not is_panel:
        send(RECEIVERS, SUBJECT_FORMAT.format(version=version, step=step.upper(), lines=lines), CONTENT)

    
if __name__ == '__main__':
    run()

