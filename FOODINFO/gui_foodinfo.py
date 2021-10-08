import pymysql 
from tkinter import * 
from tkinter import messagebox ## 함수 선언부 # btnInsert 클릭 시 호출되는 함수 
def insertData() : 
    con, cur = None, None 
    data1, data2, data3 = "", "", ""
    sql="" 
    conn = pymysql.connect(host='mgrsdp.c8ybdvubh7vg.ap-northeast-2.rds.amazonaws.com',
                           user='mgrsdp', password='ajrrjfl!',
                           db='mgrsdp', charset='utf8') 
    cur = conn.cursor() 
    data1 = edt1.get() 
    data2 = edt2.get() 
    data3 = edt3.get() 
    try : # 예외처리 시작 
        sql = """insert into foodInfo(name,info,color) values (%s, %s, %s)"""
        cur.execute(sql, (data1, data2, data3)) 
    except : # 에러발생 시 작동 
        messagebox.showerror('Error', 'Error While Saving Data') 
    else : # 에러 없을 시 작동 
        messagebox.showinfo('Success', 'Data Saved Successfully') 
    conn.commit() 
    conn.close() # btnSelect 클릭 시 호출되는 함수 
def selectData() : 
    strData1, strData2, strData3, strData4 = [], [], [], []
    conn = pymysql.connect(host='sdp-1.cw0d5ase2oqv.ap-northeast-2.rds.amazonaws.com', 
                           user='yurim', password='Bloody8*8*', 
                       db='sdpdb_1', charset='utf8') 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM foodInfo") 
    strData1.append("id") 
    strData2.append("name") 
    strData3.append("info") 
    strData4.append("color") 
    strData1.append("-----------") 
    strData2.append("-----------") 
    strData3.append("-----------") 
    strData4.append("-----------") 
    while (True) : 
        row = cur.fetchone() # 위에서 커서 실행으로 셀렉트한 테이블값을 한줄씩 row에 입력 후 다음줄로 
        if row== None : 
            break; 
        strData1.append(row[0]) # 리스트 strData1에 테이블 셀렉트한 첫번째 값 row[0] 입력 
        strData2.append(row[1]) 
        strData3.append(row[2])
        strData4.append(row[3]) 
    listData1.delete(0,listData1.size() - 1) # 리스트박스에 있는 값들을 모두 지워버림 
    listData2.delete(0,listData2.size() - 1) 
    listData3.delete(0,listData3.size() - 1) 
    listData4.delete(0,listData4.size() - 1) 

    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4): #item에 strData들을 한줄씩 입력 
        listData1.insert(END, item1) # 리스트박스 마지막줄에 item 값들을 넣어줘서 보여 
        listData2.insert(END, item2) 
        listData3.insert(END, item3) 
        listData4.insert(END, item4) 

    conn.close() ## 메인 코드부 
window = Tk() 
window.geometry("800x300") 
window.title("GUI 데이터 입력") 
edtFrame = Frame(window); 
edtFrame.pack() 
listFrame = Frame(window) 
listFrame.pack(side = BOTTOM,fill=BOTH, expand=1) 
edt1= Entry(edtFrame, width=10) 
edt1.pack(side=LEFT,padx=10,pady=10) 
edt2= Entry(edtFrame, width=10) 
edt2.pack(side=LEFT,padx=10,pady=10) 
edt3= Entry(edtFrame, width=10) 
edt3.pack(side=LEFT,padx=10,pady=10) 

btnInsert = Button(edtFrame, text="save", command = insertData) 
btnInsert.pack(side=LEFT,padx=10,pady=10) 
btnSelect = Button(edtFrame, text="view", command = selectData ) 
btnSelect.pack(side=LEFT,padx=10,pady=10) 
listData1 = Listbox(listFrame,bg = 'lightblue') 
listData1.pack(side=LEFT,fill=BOTH, expand=1) 
listData2 = Listbox(listFrame,bg = 'lightblue') 
listData2.pack(side=LEFT,fill=BOTH, expand=1) 
listData3 = Listbox(listFrame,bg = 'lightblue') 
listData3.pack(side=LEFT,fill=BOTH, expand=1) 
listData4 = Listbox(listFrame,bg = 'lightblue') 
listData4.pack(side=LEFT,fill=BOTH, expand=1) 


window.mainloop()

