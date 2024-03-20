from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

# - content
# - like
# - dislike
# - User : FK
# - Video : FK

class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # User:Comment => 1:N
        # - User => Comment, Comment Comment, ... (O)
        # - Comment => User, User, User (X)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Video:Comment => 
        # - Video => Comment, Comment, Comment, ... (O)
        # - Comment => Video, Video, Video (X)
    
    video = models.ForeignKey(Video, on_delete=models.CASCADE)