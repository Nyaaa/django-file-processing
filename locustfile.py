from locust import HttpUser, task


class StressTestUser(HttpUser):
    @task
    def get_file_list(self):
        self.client.get('/files')

    @task
    def upload_file(self):
        self.client.post('/upload/', files={'file': open('README.md')})
