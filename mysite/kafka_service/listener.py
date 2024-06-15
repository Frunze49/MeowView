from kafka import KafkaConsumer
from json import loads
import sys

from db_connector.database import Session
from db_connector.model import Statistics

from sqlalchemy import update, func

import ast

session = Session()

consumer = KafkaConsumer(
    'likes', 'views',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
)


for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}", file=sys.stderr)
    json_msg = ast.literal_eval(message.value.decode('utf-8'))
    print(f"Parse message: {json_msg['post_id'], json_msg['user_id'], json_msg['action']}", file=sys.stderr)
    if json_msg['post_id'] and json_msg['user_id']:
        user_id = json_msg['user_id']
        post_id = json_msg['post_id']
        action  = json_msg['action']

        stat = session.query(Statistics).filter_by(post_id=post_id).first()

        print(user_id, post_id, action, file=sys.stderr)

        if action == 'like':
            print("LIKE!!!", file=sys.stderr)
            if not stat:
                print("NEW!!!", file=sys.stderr)
                stat = Statistics(post_id=post_id, user_like_ids=[user_id], user_view_ids=[])
                session.add(stat)

            elif user_id not in stat.user_like_ids:
                print("APPENDED!!!", stat.user_like_ids, file=sys.stderr)
                stmt = (
                    update(Statistics).
                    where(Statistics.post_id == post_id).
                    values(user_like_ids=func.array_append(Statistics.user_like_ids, user_id))
                )
                session.execute(stmt)

        elif action == 'view':
            if not stat:
                stat = Statistics(post_id=post_id, user_like_ids=[], user_view_ids=[user_id])
                session.add(stat)

            elif user_id not in stat.user_view_ids:
                print("APPENDED!!!", stat.user_like_ids, file=sys.stderr)
                stmt = (
                    update(Statistics).
                    where(Statistics.post_id == post_id).
                    values(user_view_ids=func.array_append(Statistics.user_view_ids, user_id))
                )
                session.execute(stmt)

        elif action == 'delete_like':
            if stat and user_id in stat.user_like_ids:
                stat.remove(user_id)

        print("END!!!", stat.user_like_ids, file=sys.stderr)
        session.commit()
        


