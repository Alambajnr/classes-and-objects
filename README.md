#  User & Post Management in Python

This project demonstrates the fundamentals of **object-oriented programming (OOP)** in Python by modeling a simple social application with **Users** and **Posts**. It highlights how classes and objects can be used to represent real-world entities, encapsulate data, and define behaviors.

##  Features
- **User Class**
  - Stores user details: email, name, password, and current job title.
  - Allows updating of password and job title.
  - Provides a method to display user information in a readable format.

- **Post Class**
  - Represents a message authored by a user.
  - Stores the post content and author name.
  - Provides a method to display post details.

##  Tech Stack
- Python 3.x

##  Example Usage
```python
from user import User
from post import Post

# Create users
app_user_one = User("alamba.gmail.com", "Collins Uket", "Pwd", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("collins.gmail.com", "Collins Alamba", "Pwd", "DevOps Engineer")
app_user_two.get_user_info()

# Create a post
new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
```

###  Sample Output
```
User Collins Uket currently works as a DevOps Engineer. You can contact them at alamba.gmail.com
User Collins Alamba currently works as a DevOps Engineer. You can contact them at collins.gmail.com
Post: on a secret mission today written by Collins Alamba
```

##  Why This Project Matters
This project is a practical demonstration of:
- **Classes as blueprints** for creating structured data models.
- **Objects as instances** that hold real data and behaviors.
- Encapsulation and method usage in Python OOP.

It’s a simple but effective showcase of how Python can be used to design reusable, maintainable code — a skill highly valued in professional software development.

##  Future Improvements
- Add **authentication** (e.g., password validation or encryption).  
- Implement **timestamps** for posts to track when they were created.  
- Link posts directly to **User objects** instead of just storing the author’s name.  
- Create a **feed system** to display all posts by all users.  
- Add **unit tests** to ensure reliability and demonstrate testing best practices.  
- Expand into a **mini social app** with likes, comments, and user interactions.
