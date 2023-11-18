import new.models

sum_rating_post = 0
rating_post = ''
for i in set_rating_post:
    sum_rating_post = sum_rating_post + i
rating_post = sum_rating_post * 3
set_rating_comment_self = self.comment.rating.all()
sum_rating_comment_self = 0
for c in set_rating_comment_self:
    sum_rating_comment_self = sum_rating_comment_self + c
set_rating_comment_post = self.post.comment.rating.all()
sum_rating_comment_post = 0
for x in set_rating_comment_post:
    sum_rating_comment_post = sum_rating_comment_post + x
return print(f'суммарный рейтинг каждой статьи автора:{rating_post}'
             f'суммарный рейтинг всех комментариев автора: {sum_rating_comment_self}'
             f'суммарный рейтинг всех комментариев к статьям автора: {sum_rating_comment_post}')