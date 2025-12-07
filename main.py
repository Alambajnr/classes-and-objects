from user import User
from post import Post

app_user_one = User("alamba.gmail.com", "Collins Uket", "Pwd","Devops Engineer")
app_user_one.get_user_info()

app_user_two = User("collins.gmail.com", "Collins Alamba", "Pwd","Devops Engineer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()