import random

players = []
cell = []#cellの全て
cells = []#cells.append(cel.name)

class Cells():
    def __init__(self, name, rate ,color):
        self.name = name
        self.rate = rate
        self.color = color
###################################################################################
def set_cell():
    global cells
    for cel in cell:
        cells.append(cel.name)
def create_table():#Cellインスタンスをtebleに入れる
    global cell
    cell.append(Cells('R', 8, 'red'))
    cell.append(Cells('B', 8, 'black'))
    cell.append(Cells('1', 2, 'red'))
    cell.append(Cells('2', 2, 'black'))
    cell.append(Cells('3', 2, 'red'))
    cell.append(Cells('4', 2, 'black'))
    cell.append(Cells('5', 2, 'red'))
    cell.append(Cells('6', 2, 'black'))
    cell.append(Cells('7', 2, 'red'))
    cell.append(Cells('8', 2, 'black'))

def create_players():
    global players
    human = Human('MY' , 500)
    computer1 = Computer('C1' , 500)
    computer2 = Computer('C2' , 500)
    computer3 = Computer('C3' , 500)
    players = [human , computer1 ,computer2,computer3]
###################################################################################
class Player ():
    def __init__(self, name, coin):#コンストラクタ
        self.name = name#メンバ変数
        self.coin = coin
        self.bets = {}#[cell[0]:0 ,cell[1]:0 ,cell[2]:0 ,cell[3]:0 ,cell[4]:0  ]
        for cel in cell:#global cellの中の数字を初期化
            self.bets.update({cel.name : 0})


    def info(self):
        print(self.name , self.coin)

    def set_bet_coin(self,bet_coin , bet_cell):#bet_cellはc
        self.cell = bet_cell
        self.bet_coin = int(bet_coin)#bet_coinランダムの値
        self.bets.update({bet_cell : self.bet_coin})
        # bet_cellは'R', 'B', '1', '2', '3', '4', '5', '6', '7', '8'
        self.coin -= self.bet_coin
        print(str(self.name)+'は→→→→→→→→→'+str(self.bet_coin)+'コインを'+str(bet_cell) +'にBETしました')
        
    


class Human(Player):
    def __init__(self, name, coin):#グローバルで定義してる感じ
        super().__init__(name,coin)#__init__は継承出来ないがスーパークラスを使うと継承できる

    def enable_bet_coin(self,string):#3 '＊＊＊何枚BETしますか？
        if string.isdigit():
            string = int(string)
            if 1 <= string  <=99 :
                return True
            else:
                return False
        else: False        
    def enable_bet_cell(self,string_num):#5 文字型が数値だったら　どこにBETしますか？
        if string_num.isdigit():
            return True
        else:
            return False
            
    def bet(self):#１
        bet_coin =  input('＊＊＊何枚BETしますか？')
        while not self.enable_bet_coin(bet_coin):#2
            bet_coin =  input('何枚BETしますか？')

        bet_cell = input('どこにBETしますか？')
        while not self.enable_bet_cell(bet_cell):#4
            bet_cell = input('どこにBETしますか？')
        super().set_bet_coin(bet_coin ,bet_cell)   #親から継承している


class Computer(Player):#継承
    def __init__(self, name, coin):
        super().__init__(name, coin)#ここの変数は上の変数にも通じているよ ****書き換えられる重要
        
    def bet(self):
        if 99 <= self.coin:#99以上
            max_bit_coin = 99
        else:#99以下
            max_bit_coin = self.coin
        bet_coin = random.randint(1,max_bit_coin)
        print('ランダムの値は')
        print(bet_coin)
        cells = []#__dict__['name']['R', 'B', '1', '2', '3', '4', '5', '6', '7', '8']
        for cel in cell:
            cells.append(cel.name)#__dict__['name']['R', 'B', '1', '2', '3', '4', '5', '6', '7', '8']
        bet_cell_number = random.randint(0,len(cells) -1)
        bet_cell = cells[bet_cell_number]#どれか選ぶ
        print(str(bet_cell)+'番目seeeeeeeeeeeeeeeeeee')
        print (cells)

        super().set_bet_coin(bet_coin ,bet_cell)     #bet_coinランダムの値 bet_cellは'R', 'B', '1', '2', '3', '4', '5', '6', '7', '8'クラスの中から親クラスの関数にアクセスするときはsuperを使う
        
def show_players():
    for player in players:
        player.info()
    for player in players:#コイン値取得している　#players = [human , computer1 ,computer2,computer3]
        player.bet()
    for player in players:
        player.info()

#######################################################################################################################################
class ColorBase:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[0m'

    
def green_bar():
    return ColorBase.GREEN + '｜' + ColorBase.END
def color(self , bar):
    if self.color == 'red':
        return ColorBase.RED + '｜' + self.name + '(x' + str(self.rate) + ')｜' 
    else:
        return bar + self.name + '(x' + str(self.rate) + ')'+ bar

def show_table():
    row = green_bar() + '_____' + green_bar()#｜___｜
    for play in players:#players = [human , computer1 ,computer2,computer3]
        row += play.name + green_bar()#MY｜C1｜C2｜C3｜
    print(row)#｜___｜MY｜C1｜C2｜C3｜

    for cel in cell:#Cellテーブルを作る
        row = color(cel , green_bar())#redかblackの文字が返ってくる    [cell一つずつ　& 表示する文字を持ってくる]
        for player in players:
            row += str(player.bets[cel.name]).zfill(2)+ green_bar()#0継承してるから関数なくても使える str忘れ
        print(row)
        
        # ｜R(x8)｜
        # ｜B(x8)｜
        # ｜1(x2)｜
        # ｜2(x2)｜
        # ｜3(x2)｜
        # ｜4(x2)｜
        # ｜5(x2)｜
        # ｜6(x2)｜
        # ｜7(x2)｜
        # ｜8(x2)｜
def win_player(player , hit_cell_number):##players = [human自分 , computer1 ,computer2,computer3]        hit_cell_number10までの
    hit_cel = cell[hit_cell_number]#cell.append(Cells('R', 8, 'red'))
    win_coin = 22
    player.coin =+ win_coin#22
def check_hit():
    hit_cell_number = cells[int(random.randint(0,len(cells)))]#10
    hit_cell = cell[hit_cell_number]#cell[0~10]
    print('cellsで選ばれたのは' + hit_cell_number)#例５　 4(x2)｜00｜00｜00｜00｜
    for player in players:#players = [human自分 , computer1 ,computer2,computer3]
        if 1 <= player.bet[hit_cell] :#player.bet[cell[0]]#cell[0]には対{応した値がある　その値が００じゃなかったら　確立10分の1
            #コインの中が1以上だったらbetされているもの  cell[hit_cell_number仮に５] = self.bets = {}#[cell[0]:0 ,cell[1]:0 ,cell[2]:0 ,cell[3]:0 ,cell[4]:0  ]......
            win_player(player , hit_cell_number)#players = [human自分 , computer1 ,computer2,computer3]   #10

# if 1 <= player.bet[cell[hit_cell_number]]player.betのそれぞれ格納されている値の中が００じゃなかったら当たり



def play():
    create_table()#cellをリストに入れるcell.append(Cells('R', 8, 'red'))
    create_players()#[human , computer1 ,computer2,computer3]をリストに入れる
    set_cell()#celをリストにする
    # global cells
    # for cel in cell:
    #     cells.append(cel.name)
    # cel.nameをforでリストに格納した
    show_table()#赤青の｜R(x8)｜
                    # ｜B(x8)｜
                    # ｜1(x2)｜
                    # ｜2(x2)｜
                    # ｜3(x2)｜
                    # ｜4(x2)｜
                    # ｜5(x2)｜

    show_players()#player.info() player.bet() player.info()
    check_hit()
    show_table()
    
play()
# print(players[1].name)

print(cell)