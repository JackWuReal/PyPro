# 需求:
# 1. 设计一个 Game 类
# 2. 属性:
# • 定义一个 top_score 类属性 -> 记录游戏的历史最高分
# • 定义一个 player_name 实例属性 -> 记录当前游戏的玩家姓名
# 3. 方法:
# • 静态方法 show_help() -> 显示游戏帮助信息
# • 类方法 show_top_score() -> 显示历史最高分
# • 实例方法 start_game() -> 开始当前玩家的游戏
# - ① 使用随机数 生成 10-100 之间数字 作为本次游戏的得分
# - ② 打印本次游戏等分 : 玩家 xxx 本次游戏得分 ooo
# - ② 和历史最高分进行比较, 如果比历史最高分高, 修改历史最高分
# 4. 主程序步骤: main
# 1 查看帮助信息
# 2 查看历史最高分
# 3 创建游戏对象，开始游戏
# 4 再一次游戏

import random
class Game:

    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name


    @staticmethod
    def show_help():
        print("this is game help info")

    @classmethod
    def show_top_score(cls):
        print(cls.top_score)
        return cls.top_score

    def start_game(self):
        print(f'{self.player_name} start game')
        self.score = random.randint(10,100)
        print(f'{self.player_name}本次游戏得分：{self.score}')
        if self.score > Game.top_score:
            Game.top_score = self.score
        return


if __name__ == '__main__':

    while True:
        num = int(input("# 1 查看帮助信息# 2 查看历史最高分# 3 创建游戏对象，开始游戏# 4 再一次游戏"))
        if num == 1:
            Game.show_help()
        elif num == 2:
            Game.show_top_score()
        elif num == 3:
            play_name = input('请输入游戏人物名')
            game = Game(play_name)
            game.start_game()
        elif num == 4:
            play_name = input('请输入游戏人物名')
            game = Game(play_name)
            game.start_game()
        else:
            print("你输错了，请重新输入")

