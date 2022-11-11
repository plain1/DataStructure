#2017025073 강병욱
#모르스트리
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

table = [('A','.-'), ('B','-...'), ('C','-.-.'), ('D','-..'), ('E','.'), ('F','..-.'),
          ('G','--.'), ('H','....'), ('I','..'), ('J','.---'), ('K','-.-'), ('L','.-..'),
          ('M','--'), ('N','-.'), ('O','---'),('R','.-.'), ('S','...'), ('T','-'), ('U','..-'),
          ('V','...-'), ('W','.--'), ('X','-..-'), ('Y','-.--'), ('Y','--..'), ('Z','--..')]

def make_morse_tree():
    root = TNode(None,None,None)
    for tp in table:
        code = tp[1] #모르스 코드
        node = root
        for c in code:  #맨 마지막 문자 이전까지 --> 이동
            if c == '.': #왼쪽으로 이동
                if node.left == None: #비었으면 빈 노드 만들기
                    node.left = TNode(None,None,None)
                node = node.left #그쪽으로 이동
            elif c == '-':      #오른쪽으로 이동
                if node.right == None:  #비었으면 빈 노드 만들기
                    node.right = TNode(None,None,None)
                node = node.right   #그쪽으로 이동

def encode(ch):
    idx= ord(ch)-ord('A')   #리스트에서 문자 인덱스
    return table[idx][1]    #문자의 모스 부호 반환

def decode(root,code):
    node = root
    for c in code:  #맨마지막 문자 이전까지 --> 이동
        if c =='.':node = node.left #점(.):왼쪽으로 이동
        elif c == '-':node = node.right #선(-):오른쪽으로 이동
        
    return node.data    #문자반환

def sequential_search(A,key,low,high): #순차탐색
    for i in range(low,high+1):
        if A[i] == key: #탐색 성공하면
            return i #인덱스 반환
    return None #탐색에 실패하면 None 반환

morseCodeTree = make_morse_tree()
str = input("입력문장:")
mlist =[]
for ch in str:
    code =encode(ch)
    mlist.append(code)
print("Morse Code:",mlist)
print("Decoding:",end='')
for code in mlist:
    ch = decode(morseCodeTree,code)
    print(ch,end='')
print()