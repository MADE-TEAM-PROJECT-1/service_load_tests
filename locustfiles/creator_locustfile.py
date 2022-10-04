import json

from locust import FastHttpUser, task, constant_throughput

with open('data/foo_text.json', 'r') as file:
    foo_user = json.load(file)


class CreatorUser(FastHttpUser):
    @task
    def hello_world(self):
        self.client.post("/text/", json=foo_user)

    wait_time = constant_throughput(1)
