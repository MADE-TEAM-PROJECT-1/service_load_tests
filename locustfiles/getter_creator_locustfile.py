import json

from locust import FastHttpUser, task, constant_throughput
from random import randint

with open('data/foo_text.json', 'r') as file:
    foo_user = json.load(file)


class CreatorUser(FastHttpUser):
    @task
    def create_text(self):
        self.client.post("/text/", json=foo_user)



    @task 
    def get_texts(self):
        skip = randint(0, 10_000)
        limit = 10
        self.client.get("/texts/", params={"skip": skip, "limit" : limit})

    wait_time = constant_throughput(1)
