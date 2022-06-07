class gramatica:

    def __init__(self):
        self.l={}
        self.letras =f"[a-z]"
        self.id=f"{self.letras}*"
        self.reserved=["mysql","connector","connect","conexion","def","Class","mydb","host","user","passwd","database"]
        self.simbols2=["\-","\_","\+","\{","\}"]
        self.simbols=["\(","\)","\:","\.","\,","\=","\""]
        self.tokens=["MYSQL","CONNECTOR","CONNECT","CONEXION","DEF","CLASS","MYDB","H","US","PWD","DB","LETRA","PA","PC","DP","PT","CO","IG","CM"]
        # self.qf = f"\{self.a,self.fo,self.pa,self.id,self.pc,self.f}"
        # self.qc = f"\{self.cr,self.t,self.pa,self.id,self.pc,self.c}"
        # self.i = f"\{self.qc}\{self.puc}\{self.rr}"
        # self.sh = f".start\{self.pa}\{self.pc}"