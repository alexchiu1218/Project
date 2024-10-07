import random
# 定義姓氏和名字的數據庫
first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
last_names_single = ['Li', 'Wang', 'Chen', 'Lin']
last_names_double = ['Zhang', 'WangJian', 'ChenLong', 'LiuKun']
age = range(0,31)
class FakeUser:
    def __init__(self):
        self.first_name = self.random_first_name()
        self.last_name = self.random_last_name()
        self.gender = self.random_gender()
        self.age = self.random_age()
    # 隨機生成姓氏
    def random_last_name(self):
        if random.choice([True, False]):  # 50% 機率選擇單字姓或雙字姓
            return random.choice(last_names_single)
        else:
            return random.choice(last_names_double)
    # 隨機生成名字
    def random_first_name(self):
        return random.choice(first_names)
    # 隨機生成性別
    def random_gender(self):
        return random.choice(['Male', 'Female'])
    def random_age(self):
        return random.choice(age)
    # 返回完整的用戶信息
    def get_full_user(self):
        return f'{self.last_name} {self.first_name},{self.gender},{self.age}'
# 創建一個 FakeUser 的實例
user = FakeUser()
print('fakeuser:',user.get_full_user())
