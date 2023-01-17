from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    def __str__(self):
        return f'{self.pk} : {self.name}'



class Feed(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='feeds')
    content = models.TextField()
    like_people = models.ManyToManyField(Person, related_name='like_feeds') # 컬럼을 추가하는 것이 아니라 테이블을 만드는것임.


class Comment(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)

'''
    [related name]
p1.like_feeds.all() -> 좋아요 한 게시글 모두

    [field name]
f1.like_people.all() -> f1 게시글에 좋아요 한 사람들 모두

pl.like_feeds.add(f1) -> p1이 좋아요 한 게시글에 f1게시글 추가 ->  join 테이블에 p1, f1 레코드 추가
f1.like_people.add(p1) -> 결과 같음(데이터 중복 안됨)

p1.like_feeds.remove(f1) -> join테이블에서 p1,f1으로 구성된 레코드 삭제
f1.like_people(p1) -> 결과 같음
'''