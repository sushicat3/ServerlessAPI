from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task
    def getUsers(l):
        l.client.get("/users")

    @task
    def getPosts(l):
        l.client.get("/posts")

    # @task
    # def getSushicatPosts(l):
    #     l.client.get("/posts/users/2")

    # @task
    # def getOctocatPosts(l):
    #     l.client.get("/posts/users/4")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000