''' 2개의 클래스를 이용하여 변수 초기화, 출력문 형식 지정하기 '''
class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)


class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        self.posts.append(Post(date, content))
            # 파라미터로 받은 게시일과 내용을 Post 클래스의 인스턴스 초기화 기능으로 리스트에 추가

    def show_all_posts(self):
        # 블로그 유저의 모든 게시글 출력
        for post in self.posts:
            print(post)
                # ★실수가 있었던 부분. for i in range(0, len(self.posts) // 2)의 꼴로
                # 반복문을 작성했다. 결과는 정상적으로 출력됐지만, white space가 들어갔다.
                # 인덱스를 활용한 반복문 외에 다양한 형태에도 익숙해지돌록 노력해야겠다.


    def __str__(self):
        # 간단한 인사와 이름을 문자열로 리턴
        return "안녕하세요 {}입니다.\n".format(self.name)
            # 이와 같은 형식으로 return문의 형식을 지정해주거나, 2개 이상의 값을 반환할 수 있다.



# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()
