from kafka import KafkaConsumer
from json import loads
import sys

from db_connector.database import StatisticsSession
from db_connector.model import Statistics

from sqlalchemy import update, func, and_

import ast

session = StatisticsSession()

consumer = KafkaConsumer(
    'likes', 'views',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    api_version=(0,11,5),
)


for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}", file=sys.stderr)
    json_msg = ast.literal_eval(message.value.decode('utf-8'))
    print(f"Parse message: {json_msg['post_id'], json_msg['user_id'], json_msg['action']}", file=sys.stderr)
    if json_msg['post_id'] and json_msg['user_id'] and json_msg['action'] and 'author' in json_msg:
        user_id = json_msg['user_id']
        post_id = json_msg['post_id']
        action  = json_msg['action']
        author  = json_msg['author']

        stat = session.query(Statistics).filter_by(post_id=post_id, user_id=user_id).first()

        print(user_id, post_id, action, file=sys.stderr)

        if action == 'like':
            if not stat:
                print("NEW!!!", file=sys.stderr)
                stat = Statistics(post_id=post_id, user_id=user_id, like=True, view=False, author=author)
                session.add(stat)

            else:
                stmt = (
                    update(Statistics).
                    where(
                        and_(
                            Statistics.post_id == post_id,
                            Statistics.user_id == user_id
                        )
                    ).
                    values(like=True)
                )
                session.execute(stmt)

        elif action == 'view':
            if not stat:
                stat = Statistics(post_id=post_id, user_id=user_id, like=False, view=True, author=author)
                session.add(stat)

            else:
                stmt = (
                    update(Statistics).
                    where(
                        and_(
                            Statistics.post_id == post_id,
                            Statistics.user_id == user_id
                        )
                    ).
                    values(view=True)
                )
                session.execute(stmt)

        # elif action == 'delete_like':
        #     if stat and user_id in stat.user_like_ids:
        #         stat.remove(user_id)

        session.commit()
        


